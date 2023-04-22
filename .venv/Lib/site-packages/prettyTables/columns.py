from .cells import (
    _center_cell, 
    _ljust_cell, 
    _rjust_cell,
    _fljust_cell,
    _add_cell_spacing
)
from .style_compositions import TableComposition
from .utils import (
    is_some_instance,
    IndexCounter,
    ValuePlacer
)
from .options import (
    DEFAULT_FILL_CHAR, 
    FLT_FILTER, 
    INT_FILTER
)

from typing import (
    Any, 
    Dict, 
    List, 
    Tuple, 
    Union, 
    Generator
)
from collections import namedtuple

TypeNames = namedtuple(
    'TypeNames',
    [
        'bool_',
        'str_',
        'int_',
        'float_',
        'bytes_',
        'none_type_',
        'index_counter_',
        'value_placer_',
    ]
)


TYPE_NAMES = TypeNames(
    bool_=bool.__name__,
    str_=str.__name__,
    int_=int.__name__,
    float_=float.__name__,
    bytes_=bytes.__name__,
    none_type_=type(None).__name__,
    index_counter_=IndexCounter.__name__,
    value_placer_=ValuePlacer.__name__,
)


FLOAT_SEPARATOR = '.'


ALIGNMENTS_PER_TYPE = {
    TYPE_NAMES.bool_: 'r',
    TYPE_NAMES.str_: 'l',
    TYPE_NAMES.int_: 'r',
    TYPE_NAMES.float_: 'f',
    TYPE_NAMES.bytes_: 'b',
    TYPE_NAMES.none_type_: 'l',
}


CAN_WRAP_TYPES = [
    TYPE_NAMES.str_,
    TYPE_NAMES.none_type_,
    TYPE_NAMES.value_placer_
]


def __check_for_types_in_column(column_types: list, 
                                accepted_types: list
                               ) -> bool:
    """
    Compares two list of type names.
    
    Example::

        __check_for_types_in_column(
            column_types=['str', 'int'], 
            accepted_types=['str', 'int']
        ) -> True
        __check_for_types_in_column(
            column_types=['str', 'int', 'float'], 
            accepted_types=['str', 'int']
        ) -> False
    """
    for type_ in column_types:
        if type_ not in accepted_types:
            return False
                
    return True


def __is_str_column(column_types: list) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those::
    
        'bool',         'str',         'int', 
        'float',        'bytes',       'NoneType',
        'IndexCounter'  'ValuePlacer' 
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=list(TYPE_NAMES)
    )
    return test


def __is_byte_column(column_types: list) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those:: 
    
        'bytes', 'ValuePlacer' 
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=[
            TYPE_NAMES.bytes_,
            TYPE_NAMES.value_placer_
        ]
    )
    return test


def __is_int_column(column_types: list) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those::
    
        'int', 'bool', 'ValuePlacer', 'IndexCounter' 
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=[
            TYPE_NAMES.int_,
            TYPE_NAMES.bool_,
            TYPE_NAMES.value_placer_,
            TYPE_NAMES.index_counter_
        ]
    )
    return test
    
    
def __is_float_column(column_types: list) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those:: 
    
        'int', 'float', 'ValuePlacer'
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=[
            TYPE_NAMES.int_,
            TYPE_NAMES.float_,
            TYPE_NAMES.value_placer_,
        ]
    )
    return test


def __is_bool_column(column_types: bool) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those:: 

        'bool', 'ValuePlacer'
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=[
            TYPE_NAMES.bool_,
            TYPE_NAMES.value_placer_
        ]
    )
    return test


def __is_none_type(column_types: list) -> bool:
    """
    Receives a list of type names and returns True if
    all of the names are one of those::

        'NoneType', 'ValuePlacer'
    """
    test = __check_for_types_in_column(
        column_types=column_types,
        accepted_types=[
            TYPE_NAMES.none_type_,
            TYPE_NAMES.value_placer_
        ]
    )
    return test


def __get_column_type(column_types):
    """
    Will return the type of the column depending
    on what combination of types it has.
    
    Examples::
    
        __get_column_type(['str', 'int']) -> 'str'
        __get_column_type(['ValuePlacer', 'int']) -> 'int'
        __get_column_type(['float', 'int']) -> 'float'
        __get_column_type(['NoneType', 'int']) -> 'str'
        __get_column_type(['ValuePlacer', 'bool']) -> 'bool'
    """
    if __is_none_type(column_types):
        return TYPE_NAMES.none_type_
    # if __is_byte_column(column_types):
    #     return TYPE_NAMES.bytes_
    if __is_bool_column(column_types):
        return TYPE_NAMES.bool_
    if __is_int_column(column_types):
        return TYPE_NAMES.int_
    if __is_float_column(column_types):
        return TYPE_NAMES.float_
    if __is_str_column(column_types):
        return TYPE_NAMES.str_
    else:
        return TYPE_NAMES.none_type_
    
    
def __header_width(header: Union[Any, list, tuple]) -> int:
    """
    Returns the width of the header.
    """
    if is_some_instance(header, tuple, list):
        # If it's wrapped, will be a tuple or list. To get
        # the size, will get first the lengths of all the sub-rows
        # and the the max of them.
        return (
            max([len(str(sub_row)) for sub_row in header])
        )
    else:
        # If it's not wrapped, will be a string, so will only
        # get it's length.
        return len(str(header))


def __get_single_column_width(column: dict, 
                             show_headers: bool
                            ) -> Tuple[int, int]:
    """
    Will return the max size of the data in the column
    and the header size.
    
    Should receive a column with one of the following structures::

        # WITH WRAPPED HEADER AND DATA
        {
            'header': (('wrapped', 'header'), ...), 
            'data': ('data', ('wrapped', 'cell'), ...)
        }
        
        # NO WRAPPER HEADER OR DATA
        {
            'header': 'header1', 
            'data': ('data', ...)
        }
    
    Returns::

        (header_size: int, body_max_size: int)
    """
    head_size = 0
    body_sizes = []
    if show_headers:
        # If headers will show, get them.
        header = column['header']
        head_size += __header_width(header)
    for row in column['data']:
        # The same principle as the header is applied here but for each cell.
        # Every length will be added to the body_sizes list.
        if is_some_instance(row, tuple, list):
            body_sizes.append(
                max([len(str(sub_row)) for sub_row in row])
            )
        else:
            body_sizes.append(len(str(row)))
    
    # And once more will get the max to get the length of the column.
    body_max_size = max(body_sizes)
            
    return head_size, body_max_size

def __get_float_widths(cell: str, 
                       is_float: bool,
                       head_size: int,
                       max_widths_of_sides: List[int],
                      ) -> Tuple[Tuple[int, int, int], bool]:
    """
    Will get the widths of the three sides of a 
    cell in a float column and will determine wether the
    left side should be reduced or not.
    
    Returns::
    
        (sides_widths: tuple, reduce: float)
    
    Examples::
    
        __get_float_widths(
            cell="missing_value__",
            is_float=None,
            head_size=8,
            max_widths_of_sides=[]
        ) -> ((15, 0, 0), True)
        
        __get_float_widths(
            cell="missing_value__",
            is_float=None,
            head_size=8,
            max_widths_of_sides=[15, 0, 0]
        ) -> ((), False)
        
        __get_float_widths(
            cell="12.4325",
            is_float=True,
            head_size=8,
            max_widths_of_sides=[15, 0, 0]
        ) -> ((2, 1, 4), False)
        
        __get_float_widths(
            cell="111.22",
            is_float=True,
            head_size=8,
            max_widths_of_sides=[10, 1, 4]
        ) -> ((3, 1, 2), False)
    """
    sides_widths = []
    row_len = len(cell)
    reduce = False
    
    # If there's was a previous float, max len of sides should
    # have it's widths
    biggest_float_yet = sum(max_widths_of_sides)
    # so the biggest one yet is compared with the header
    header_is_bigger = head_size > biggest_float_yet
    
    if header_is_bigger:
        # If the header is bigger, the column width is the same.
        current_column_size = head_size
    else:
        # In the other case, is the sum of the biggest float yet.
        current_column_size = biggest_float_yet
        
    if is_float and is_float is not None:
        # If it is a float number, split it by the point, get the
        # widths of each side and the point
        all_sides = cell.split(FLOAT_SEPARATOR)
        sides_widths.append(len(all_sides[0]))
        sides_widths.append(len(FLOAT_SEPARATOR))  # Size of the dot
        sides_widths.append(len(all_sides[1]))
    elif not is_float and is_float is not None:
        # If it is an int just put the width of it at the left
        # side.
        sides_widths.append(row_len)
        sides_widths.append(0)  # No dot
        sides_widths.append(0) 
    else:
        # In any other case, check if the width of the data in the
        # cell is bigger than the current column size.
        if row_len > current_column_size:
            # If it is . . .
            sides_widths.append(row_len)
            sides_widths.append(0)  # No dot
            sides_widths.append(0)
            
            # Reducing the left space should be done.
            reduce = True

    sides_widths = tuple(sides_widths)

    return sides_widths, reduce


def __compare_one_side(side_i: int, 
                       sides_len: list, 
                       max_len_of_sides: list,
                       head_size: int,
                      ) -> None:
    """
    If the current cell side is bigger than the maximum,
    the last will be replaced with the first.
    """
    current_side_len = sides_len[side_i]
    if current_side_len > max_len_of_sides[side_i]:
        max_len_of_sides[side_i] = current_side_len

                
def __float_col_total_width(max_len_of_sides: list,
                            head_size: int,
                           ) -> int:
    """
    will get the width of the column based on the header
    and the som of the ``max_len_of_sides``.
    """
    sum_of_len_of_sides = sum(max_len_of_sides)
    if sum_of_len_of_sides < head_size > 0:
        max_len_of_sides[0] += head_size - sum_of_len_of_sides
        sum_of_len_of_sides = sum(max_len_of_sides)
        
    return sum_of_len_of_sides


def __get_sides_widths(cell: Any,
                       max_len_of_sides: list,
                       head_size: int,
                       will_reduce: bool,
                      ) -> bool:
    """
    Get the sides widths of a float cell.
   
    Example with float::

        123.45
        # left: 123  3
        # dot:  .    1
        # right: 45  2
    
    With string::

        'missing_value__'
        # left: missing_value__  15
        # dot:                   0
        # right:                 0
    """
    
    # Convert the row to a string in case it's not, to process
    # always the same way (could have used isinstance, but this
    # way was choose to also process floats that comes as a string).
    row_ = str(cell)
    is_float = FLT_FILTER(row_) is not None
    is_int = INT_FILTER(row_) is not None
    amount_to_reduce = 0
    
    if is_float:
        # Process as float (align by dot).
        sides_len, reduce = __get_float_widths(
            row_, 
            is_float=True,
            max_widths_of_sides=max_len_of_sides,
            head_size=head_size
        )
    elif is_int:
        # Process as int (align with the left 
        # side of the floats).
        sides_len, reduce = __get_float_widths(
            row_, 
            is_float=False,
            max_widths_of_sides=max_len_of_sides,
            head_size=head_size
        )
    else:
        # Process as string (align to the right).
        sides_len, reduce = __get_float_widths(
            row_, 
            is_float=None,
            max_widths_of_sides=max_len_of_sides,
            head_size=head_size
        )
        
    # If there's somehow an element bigger than the float sides,
    # the left side of the "max_len_of_sides" will be reduced.
    if will_reduce is True:
        # When this happens, the sum of the width of the float point
        # and all the digits after (right side) is the amount to reduce, because
        # if it isn't done, a blank space of this size is left.
        try:
            amount_to_reduce = sides_len[-1] + len(FLOAT_SEPARATOR)
        except IndexError:
            pass
    if amount_to_reduce > 0:
        # This is checked because if this "bigger element" appears first
        # that any float, the right part is 0 (no digits  after the dot yet).
        max_len_of_sides[0] -= amount_to_reduce
        
        # This is to indicate the "__get_float_col_widths" function that
        # the "float_sides_will_reduce" must be set to False.
        # This instead of False because reduce could already be False
        # wen receiving value from "__get_float_widths".
        reduce = None
         
    for side_i in range(len(sides_len)):
        try:
            __compare_one_side(
                side_i=side_i,
                sides_len=sides_len,
                max_len_of_sides=max_len_of_sides,
                head_size=head_size
            )
        except IndexError:
            max_len_of_sides.append(sides_len[side_i])
    
    return reduce


def __get_float_column_width(column: dict, 
                             show_headers: bool
                            ) -> Tuple[int, int, Tuple[int, int, int]]:
    """
    Will get the header size, body size and the max size of the sides
    of a float column.
    
    Returns::
    
        (head_size: int, sum_of_len_of_sides: int, max_len_of_sides: tuple)
    
    Example::
    
        __get_float_column_width(
            column={
                'header': ('Test', 'Results'), 
                'data': (9.651, 3, 245.7, (3.5, ''), '?')
            },
            show_headers=False
        )
    
    Results in::
    
        [0, 7, (3, 1, 3)]
    
    """
    
    head_size = 0
    if show_headers:
        # If headers will show, get them.
        header = column['header']
        head_size += __header_width(header)
    
    max_len_of_sides = []
    float_sides_will_reduce = False
    for row in column['data']:
        
        # Get the sides of row (cell) or sub-row.
        if is_some_instance(row, tuple, list):
            for sub_row in row:
                reduce = __get_sides_widths(
                    cell=sub_row,
                    max_len_of_sides=max_len_of_sides,
                    head_size=head_size,
                    will_reduce=float_sides_will_reduce
                    )
        else:
            reduce = __get_sides_widths(
                cell=row,
                max_len_of_sides=max_len_of_sides,
                head_size=head_size,
                will_reduce=float_sides_will_reduce
                )
        
        if reduce:
            float_sides_will_reduce = True
        elif reduce is None:
            float_sides_will_reduce = False
            
    sum_of_len_of_sides = __float_col_total_width(
        max_len_of_sides=max_len_of_sides,
        head_size=head_size
    )
    max_len_of_sides = tuple(max_len_of_sides)
    
    return head_size, sum_of_len_of_sides, max_len_of_sides


def _column_widths(processed_columns: Dict[str, tuple], 
                  column_type_names: dict, 
                  show_headers: bool
                 ) -> Tuple[tuple, Union[None, dict]]:
    """
    Will return the widths of the columns. Float columns widths
    are calculated by side of the point.
    
    Returns::

        (widths: tuple, float_column_widths: None | dict)
    
    Example::

        _column_widths(
            processed_columns={
                {'header': 'header1', 'data': ['data1', 'data2']},
                {'header': 'header2', 'data': [1.2, 12.43]}
            },
            column_type_names={'header1': 'str', 'header2': 'float'},
        )
    
    Results in::

        ((7, 7), {'header2': (4, 1, 2)})
    """
    # TODO add support for coloring codes

    head_sizes = []
    body_sizes = []
    float_column_widths = None
    for header, column in processed_columns.items():
        if column_type_names[header] == TYPE_NAMES.float_:
            
            # If it's a float column, get the body size, 
            # header size and float sizes.
            head_size, body_size, decimal_sides = __get_float_column_width(
                column,
                show_headers
            )
            
            # Save header and body size separately to prevent 
            # the header size # from being added to the 
            # calculation in case of turning off the headers.
            head_sizes.append(head_size)
            body_sizes.append(body_size)
            
            # Save float column sizes as a dict.
            try:
                float_column_widths[header] = decimal_sides
            except TypeError:
                float_column_widths = {header: decimal_sides}
                
        else:
            
            # If it's not a float column, get the body and header size,
            # and save them separately.
            head_size, body_size = __get_single_column_width(
                column, 
                show_headers
            )
            head_sizes.append(head_size)
            body_sizes.append(body_size)

    if show_headers:
        # Get the max width between the header and body sizes if the header
        # is set to show.
        widths = list(map(lambda x, y: max(x, y), head_sizes, body_sizes))
        
    else:
        # Only the body sizes if the header is not set to show.    
        widths = body_sizes

    return widths, float_column_widths


def _typify_column(column: Union[list, tuple], 
                   index_column=False,
                  ) -> Tuple[Tuple[str], str, str]:  
    """
    Get the types of the column and it's alignments.
    
    Uses the ``__name__`` property to get the type class' name
    traversing the column and using the ``type`` class do so::

        type(data).__name__
    
    Returns::

        (identified_types: tuple, column_type: str, column_alignment: str)
    """
    identified_types = []

    for row in column:
        if index_column:
            # If it is the index column, it will be took in count as int.
            identified_types.append(int.__name__)
        elif row != '':
            # Get the type as long as is not an empty string.
            identified_types.append(type(row).__name__)
        else:
            # If it's an empty string, should be considered as None.
            identified_types.append(type(None).__name__)

    # Get the type of the column.
    column_type = __get_column_type(identified_types)
    # Using the column type, get the alignment.
    column_alignment = ALIGNMENTS_PER_TYPE[column_type]
    identified_types = tuple(identified_types)

    return identified_types, column_type, column_alignment


def __align_single_cell(cell: Union[Any, List[Any], Tuple[Any]],
                        col_width: int, 
                        to_where: str, 
                        margin: int, 
                        float_column_sizes: list=None
                       ) -> Union[str, Tuple[str]]:
    """
    Will add space to the cell to align it.
    
    Returns::

        new_cell: str | tuple
    
    Examples::

        __align_single_cell(
            cell="data1",
            col_width=7,
            to_where="l",
            margin=1,
            float_column_sizes=None
        )
        __align_single_cell(
            cell="missing_value__",
            col_width=15,
            to_where="f",
            margin=1,
            float_column_sizes=(10, 1, 4)
        )
        __align_single_cell(
            cell=12.4325,
            col_width=15,
            to_where="f",
            margin=1,
            float_column_sizes=(10, 1, 4)
        )
        __align_single_cell(
            cell=111.22,
            col_width=15,
            to_where="f",
            margin=1,
            float_column_sizes=(10, 1, 4)
        )
    
    Results in::
    
        ' data1   '
        ' missing_value__ '
        '         12.4325 '
        '        111.22   '
    """
    new_cell = cell
    if to_where == 'l':
        # Adjust the cell to the left.
        new_cell = _ljust_cell(
            cell, 
            col_width, 
            DEFAULT_FILL_CHAR
        )
    elif to_where == 'c':
        # Adjust the cell to the center.
        new_cell = _center_cell(
            cell, 
            col_width, 
            DEFAULT_FILL_CHAR
        )
    elif to_where == 'r':
        # Adjust the cell to the right.
        new_cell = _rjust_cell(
            cell, 
            col_width, 
            DEFAULT_FILL_CHAR
        )
    elif to_where == 'f':
        # Adjust the cell as a float.
        new_cell = _fljust_cell(
            cell, 
            col_width, 
            float_column_sizes,
            DEFAULT_FILL_CHAR, 
        )
    # Add the margin (if any) to the cell.
    new_cell = _add_cell_spacing(new_cell, margin, margin, 0)
    
    if is_some_instance(new_cell, tuple, list):
        return tuple(new_cell)
    else:
        return new_cell


def __align_one_column(column: Union[list, tuple],
                       column_i: int, 
                       col_alignments: list, 
                       col_widths: list, 
                       margin: int, 
                       float_column_sizes: dict = None
                      ) -> Generator[str, None, None]:
    """
    Aligns a single row of a column.
    
    Yields::
    
        aligned_column: Generator[str]
    """
    aligned_column = []
    to_where = col_alignments[column_i]
    col_width = col_widths[column_i]
    for cell in column:
        aligned_column.append(
            __align_single_cell(
                cell, 
                col_width, 
                to_where, 
                margin,
                float_column_sizes
            )
        )

    yield tuple(aligned_column)


def _align_columns(style_composition: TableComposition, 
                   columns: Union[List[Union[list, tuple]], Tuple[Union[list, tuple]]],
                   headers: Union[list, tuple],
                   col_alignments: List[str], 
                   col_widths: List[int],
                   empty_columns_i: List[int], 
                   show_empty: bool, 
                   float_cols_sizes: dict
                  ) -> Generator[str, None, None]:
    """
    Aligns the columns and adds margin to the cells.
    """
    # The margin that the selected style has.
    margin = style_composition.margin
    
    for column_i, column in enumerate(columns):
        
        # Align only the columns that are shown.
        if (not show_empty and column_i not in empty_columns_i
        ) or show_empty:

            # Get the header of the column.
            header = headers[column_i]
            
            # Try to get the float sizes (if it is a float column).
            try:
                float_column_sizes = float_cols_sizes[header]
            except KeyError:
                float_column_sizes = None
                
            # Align the column.
            yield from __align_one_column(
                column, 
                column_i, 
                col_alignments, 
                col_widths, 
                margin,
                float_column_sizes
            )
            
        else:
            continue
    
        
def __align_one_header(column: Union[str, list, tuple], 
                       col_width: int, 
                       to_where: str, 
                       margin: int, 
                       float_column_sizes: dict
                      ) -> Union[str, Tuple[str]]:
    """
    Aligns a single cell of the header.
    """
    # Check if it's a wrapped cell.
    if is_some_instance(column, tuple, list):
        # Apply to each sub-row.
        yield tuple(map(
            lambda cell: __align_single_cell(
                cell, 
                col_width, 
                to_where, 
                margin,
                float_column_sizes
            ),
            column
        ))
    else:
        # Apply to the cell.
        yield __align_single_cell(column, col_width, to_where, margin)


def _align_headers(style_composition: TableComposition, 
                   headers: Union[list, tuple],
                   col_alignments: List[str], 
                   col_widths: List[int],
                   empty_columns_i: List[int], 
                   show_empty: bool,
                   float_cols_sizes: dict):
    """
    Will align the headers using the provided column alignments.
    """
    
    # The margin that the selected style has.
    margin = style_composition.margin
    
    for column_i, column in enumerate(headers):
        # Get the alignment of the current column.
        to_where = col_alignments[column_i]
        
        # Get the width that the current column should have.
        col_width = col_widths[column_i]
        
        # Get the column name to try to get the float sizes (in case of the
        # column a float column).
        if is_some_instance(column, tuple, list):
            # If it's wrapped, it will come splitted
            col_name = ''.join(column)
        else:
            col_name = column
        try:
            float_column_sizes = float_cols_sizes[col_name]
        except KeyError:
            float_column_sizes = None
            
        # Only align the headers if its column is shown.
        if (not show_empty and column_i not in empty_columns_i
        ) or show_empty:
            yield from __align_one_header(
                column, 
                col_width, 
                to_where, 
                margin,
                float_column_sizes
            )
        else:
            continue
             


if __name__ == '__main__':
    print('Hey! This is not to be executed.')
