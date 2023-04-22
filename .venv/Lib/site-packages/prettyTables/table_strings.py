""" TABLE SEPARATORS """

from .style_compositions import (
    HorizontalComposition, 
    TableComposition, 
    SeparatorLine
)
from .options import NONE_VALUE_REPLACEMENT
from .utils import is_multi_row

from typing import Any, List, Generator, Union
from collections import namedtuple


# The actual rows containing the table data
DataRows = namedtuple(
    'DataRows',
    [
        'header_row',
        'body_rows'
    ]
)


def __check_if_none(value):
    """
    If value is None, return the default value
    for it.
    """
    return value if value is not None else NONE_VALUE_REPLACEMENT


def __get_horizontal_line_group(line_style: SeparatorLine, 
                                widths: tuple, 
                                margin: int,
                                empty_column_i: List[int], 
                                show_empty: bool
                               ) -> Generator[str, None, None]:
    """
    This creates a group of horizontal lines for all the columns
    using the ``middle`` part of the provided ``line_style``.
    
    Should be used for every ``SeparatorLine`` group of the 
    ``HorizontalComposition``.
    
    Yields::

        horizontal_group_line: str
        
    The size of the group depends on the quantity of columns.
    The quantity of columns is determined by the quantity
    of ``widths`` which also indicates the size of the group
    lines.
    
    For example::
    
        # Having 3 columns, its widths being:
        (10, 5, 9)
        # Using this line_style:
        SeparatorLine(left='├', middle='─', intersection='┼', right='┤')
        # Having a margin of 1, the result is:
        (
            '────────────', # Size 12
            '───────',      # Size 7
            '───────────'   # Size 11
        )
    """

    # Create a line for each column (width)    
    for width_i, width in enumerate(widths):
        
        # Do it only if the column is shown
        if (not show_empty and width_i not in empty_column_i
        ) or show_empty:
            
            # Check if the middle of that style is not None (empty)
            middle = __check_if_none(line_style.middle)
            
            horizontal_group_line =  middle * (width + margin)
            yield horizontal_group_line
            
        else:
            pass


def __join_group(line_style: SeparatorLine, 
                 group: Generator[str, None, None]
                ) -> Generator[str, None, None]:
    """
    Joins a horizontal group of lines using the ``left``, ``middle``,
    and ``intersection`` parts of the provided ``line_style``.
    
    Should be used for every ``SeparatorLine`` group of the 
    ``HorizontalComposition`` and every horizontal line group
    created out of it.
    
    Yields::

        joined_group: str
        
    Example::
    
        # Using this line_style:
        SeparatorLine(left='├', middle='─', intersection='┼', right='┤')
        # And having this horizontal group:
        ('────────────', '───────', '───────────')
        # The result is:
        '├────────────┼───────┼───────────┤'
        
    """
    # Getting the parts of the line.
    left = __check_if_none(line_style.left)
    right = __check_if_none(line_style.right)
    intersection = __check_if_none(line_style.intersection)
    
    # Joining the horizontal group of lines with the intersection.
    center = intersection.join(group)
    
    # Joining the left, center and right parts.
    joined_group = ''.join([left, center, right])

    yield joined_group


def __get_column_lines(line_styles: List[SeparatorLine], 
                       widths: tuple, 
                       margin: int,
                       empty_column_i: List[int], 
                       show_empty: bool
                      ) -> Generator[str, None, None]:
    """
    Will get all the horizontal separators for the table based on
    the ``widths`` of the columns (as long as the column is shown)
    and the ``line_styles``
    """
    for line_style in line_styles:
        if line_style is not None:
            yield from __join_group(
                line_style, 
                __get_horizontal_line_group(
                    line_style,
                    widths, 
                    margin,
                    empty_column_i,
                    show_empty
                )
            )
        else:
            yield None


def _get_separators(style_composition: TableComposition, 
                    col_widths: tuple,
                    empty_column_i: List[int], 
                    show_empty: bool
                   ) -> HorizontalComposition:
    """
    Get the horizontal separators for the table.
    
    returns::
    
        horizontal_composition: HorizontalComposition
        
    A HorizontalComposition contains the following properties::
    
        superior_header_line
        inferior_header_line
        superior_header_line_no_header
        table_body_line
        table_end_line
        
    Its contents could look similar to::
    
        HorizontalComposition(
            superior_header_line='╔═══════════════════════════╗', 
            inferior_header_line='╚═══════════════════════════╝', 
            superior_header_line_no_header='┌─────────┬─────────────────┐', 
            table_body_line='├─────────┼─────────────────┤', 
            table_end_line='└─────────┴─────────────────┘'
        )
        
        HorizontalComposition(
            superior_header_line='---------------------------', 
            inferior_header_line='---------------------------', 
            superior_header_line_no_header='---------------------------', 
            table_body_line=None, 
            table_end_line='---------------------------'
        )
    


    """
    
    # Get each SeparatorLine class and save it in a variable
    # marked as the same type.
    superior_header: SeparatorLine = (
        style_composition.superior_header_line
    )
    superior_no_header: SeparatorLine = (
        style_composition.superior_header_line_no_header
    )
    inferior_header: SeparatorLine = (
        style_composition.inferior_header_line
    )
    table_body: SeparatorLine = (
        style_composition.table_body_line
    )
    table_end: SeparatorLine = ( 
        style_composition.table_end_line
    )
    
    # Get the margin as an int multiplied by the sides of the margin.
    # |margin-content-margin|
    margin: int = style_composition.margin * 2  

    # Save the SeparatorLines in a list. These are the styles of all the type
    # of lines there could be in the table.
    line_styles = [
        superior_header, 
        inferior_header, 
        superior_no_header, 
        table_body, 
        table_end
    ]
    
    # Process the horizontal separators.
    separator_lines = __get_column_lines(
        line_styles, 
        col_widths, 
        margin,
        empty_column_i,
        show_empty
    )

    # Create a HorizontalComposition object and pass the separator lines.
    horizontal_composition = HorizontalComposition(*separator_lines)

    return horizontal_composition


def __join_sub_row(left: str,
                   middle: str,
                   right: str,
                   sub_row: Any,
                  ) -> str:
    """
    Join a row or sub_row with the ``left``, ``middle`` and ``right`` 
    elements.
    
    Returns a::
    
        joined_sub_row: str
    """
    # First join the row using the middle separator. The, join the left
    # the row joined with the middle and the right.
    sub_row_joined_with_middle = middle.join(sub_row)
    joined_sub_row = ''.join([left, sub_row_joined_with_middle, right])
    return joined_sub_row


def __get_data_row(left: str, 
                   middle: str, 
                   right: str, 
                   row: Any
                  ) -> str:
    """
    Transforms the aligned data cells into a string row.
    
    For instance::

        (' data3   ', '         12.4325 ')
        (' data4   ', '        111.22   ')
        
    Turns into::
    
        '│ data3   │         12.4325 │'
        '│ data4   │        111.22   │'

    """
    if is_multi_row(row):
        # If the row is wrapped, join for each sub-row and join
        # all the sub rows with a new_line character to form
        # a single 
        joined_sub_rows = '\n'.join(
            (__join_sub_row(
                left=left, 
                middle=middle, 
                right=right, 
                sub_row=sub_row
             )
             for sub_row in row)
        )
        return joined_sub_rows
    else:
        joined_row = __join_sub_row(
            left=left, 
            middle=middle, 
            right=right, 
            sub_row=row,
        )
        return joined_row


def _get_data_rows(style_composition: TableComposition, 
                   header: tuple, 
                   body: tuple, 
                   show_headers: bool,
                   empty_rows_i: List[int], 
                   show_empty_rows: bool) -> DataRows:
    """
    Receives aligned cells and joins them with the vertical separators
    of the given ``style_composition``.
    
    Returns::
    
        data_rows: DataRows
        
    The properties of DataRows are::
    
        header_row
        body_rows
        
    Results could look like::

        DataRows(
            header_row='│ header1 │        column 2 │', 
            body_rows=(
                '│ data1   │ missing_value__ │', 
                '│ data2   │ missing_value__ │', 
                '│ data3   │         12.4325 │', 
                '│ data4   │        111.22   │', 
                '│ data5   │ missing_value__ │', 
                '│ data6   │          0.4    │', 
                '│ data7   │     321111      │')
        )

    """
    
    # Process header only if it will be shown.
    if show_headers:
        # Get the vertical separators for the header.
        header_lines: SeparatorLine = style_composition.vertical_header_lines
        header_left = __check_if_none(header_lines.left)
        header_middle = __check_if_none(header_lines.middle)
        header_right = __check_if_none(header_lines.right)
        
        # Process header.
        str_header = __get_data_row(
            header_left, 
            header_middle, 
            header_right, 
            header
        )
        
    else:
        str_header = None

    # Get the vertical separators for the body (rows).
    body_lines: SeparatorLine = style_composition.vertical_table_body_lines
    body_left = __check_if_none(body_lines.left)
    body_middle = __check_if_none(body_lines.middle)
    body_right = __check_if_none(body_lines.right)
    
    # Process each row.
    strs_body = [] 
    for row_i, row in enumerate(body):
        
        # Process only rows that will be shown.
        if (not show_empty_rows and row_i not in empty_rows_i
        ) or show_empty_rows:
            strs_body.append(__get_data_row(
                body_left, 
                body_middle, 
                body_right, 
                row
            ))
            
        else:
            pass
    
    # Dump in a DataRows object.
    data_rows = DataRows(str_header, tuple(strs_body))
    
    return data_rows


if __name__ == '__main__':
    print('Don\'t do it')
