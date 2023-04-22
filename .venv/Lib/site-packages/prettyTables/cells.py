""" CELL WRAPPING AND ADJUSTMENT """

from .utils import is_some_instance
from .options import FLT_FILTER, INT_FILTER

from typing import Any, List, Tuple, Union

LEFT_SIDE_WIDTH_I = 0
POINT_WIDTH_I = 1
RIGHT_SIDE_WIDTH_I = -1
LEFT_SIDE_I = 0
RIGHT_SIDE_I = 1

def _add_cell_spacing(cell: Union[str, Union[List[str], Tuple[str]]], 
                      left: int, 
                      right: int, 
                      placeholder_size: int = 0,
                      fill_char: str = ' '
                     ) -> Union[str, Tuple[str]]:
    """
    Add spacing to a cell (string).
    
    Examples::
    
        _add_cell_spacing('a', 1, 3, 0) -> ' a   '
        _add_cell_spacing('', 1, 3, 1)  -> '     '
        _add_cell_spacing(['a', 'b'], 1, 3, 0) -> (' a   ', ' b   ')
        _add_cell_spacing('', 1, 3, 0)  -> '    '
    """
    left = fill_char * left  # Space for the left
    right = fill_char * right  # Space for the right
    
    # Creates a string of the desired size
    # to be a placeholder when an empty string is received
    # in the cell parameter.
    diff = fill_char * placeholder_size  

    # Check if the cell is a wrapped cell (list or tuple):
    if is_some_instance(cell, tuple, list):
        # If it is, add the spacing to each part of the cell.
        spaced = list(map(str, cell))  # Convert to strings to prevent errors.
        for part_i, cell_part in enumerate(cell):
            # Add the spacing to the cell part.
            # FIX should consider the cell_part length
            if placeholder_size != 0 and part_i != 0: 
                spaced[part_i] = ''.join([left, diff, right])
            else:
                spaced[part_i] = ''.join([left, cell_part, right])
    else:
        # If it is not, add the spacing to the cell.
        # FIX should consider the cell length
        if placeholder_size != 0:
            spaced = ''.join([left, diff, right])
        else:
            spaced = ''.join([left, cell, right])

    return spaced

def _center_cell(cell: Union[str, Union[List[str], Tuple[str]]], 
                 cell_length: int, 
                 fill_char: str = ' '
                ) -> Union[str, Tuple[str]]:
    """
    Center a cell. Uses ``str().center()`` but can also center
    wrapped cells (lists or tuples).
    
    Examples::
    
        _center_cell('a', 3, '-') -> '-a-'
        _center_cell(['a', 'b'], 3, '-') -> ('-a- ', '-b-')
    """
    # Check if the cell is a wrapped cell (list or tuple):
    if is_some_instance(cell, tuple, list):
        # If it is, center each part of the cell.
        centered = list(map(str, cell))  # Convert to strings to prevent errors.
        for part_i, cell_part in enumerate(centered):
            # Center the cell part.
            centered[part_i] = cell_part.center(cell_length, fill_char)
        centered = tuple(centered)
    else:
        # If it is not, center the cell.
        centered = str(cell).center(cell_length, fill_char)

    return centered


def _ljust_cell(cell: Union[str, Union[List[str], Tuple[str]]],
                cell_length: int, 
                fill_char: str = ' '
               ) -> Union[str, Tuple[str]]:
    """
    Aligns to the left a cell. Uses ``str().ljust()`` but can also 
    align wrapped cells (lists or tuples).
    
    Examples::
    
        _ljust_cell('a', 3, '-') -> 'a--'
        _ljust_cell(['a', 'b'], 3, '-') -> ('a--', 'b--')
    """
    # Check if the cell is a wrapped cell (list or tuple):
    if is_some_instance(cell, list, tuple):
        # If it is, align each part of the cell.
        left_adjusted = list(map(str, cell)) # Convert to strings to prevent errors.
        for part_i, cell_part in enumerate(left_adjusted):
            # Align the cell part to the left.
            left_adjusted[part_i] = cell_part.ljust(cell_length, fill_char)
        left_adjusted = tuple(left_adjusted)
    else:
        # If it is not, align the cell to the left.
        left_adjusted = str(cell).ljust(cell_length, fill_char)

    return left_adjusted


def _rjust_cell(cell: Union[str, Union[List[str], Tuple[str]]],
                cell_length: int, 
                fill_char: str = ' '
               )-> Union[str, Tuple[str]]:
    """
    Aligns to the right a cell. Uses ``str().rjust()`` but can also 
    align wrapped cells (lists or tuples).
      
    Examples::

        _rjust_cell('a', 3, '-') -> '--a'
        _rjust_cell(['a', 'b'], 3, '-') -> ('--a', '--b')
    """
    # Check if the cell is a wrapped cell (list or tuple):
    if is_some_instance(cell, list, tuple):
        # If it is, align each part of the cell.
        right_adjusted = list(map(str, cell)) # Convert to strings to prevent errors.
        for part_i, cell_part in enumerate(right_adjusted):
            # Align the cell part to the right.
            right_adjusted[part_i] = cell_part.rjust(cell_length, fill_char)
        right_adjusted = tuple(right_adjusted)
    else:
        # If it is not, align the cell to the right.
        right_adjusted = str(cell).rjust(cell_length, fill_char)

    return right_adjusted


def fljust(string: str,
           sides_widths: Union[List[int], Tuple[int, int]], 
           fill_char: str=' ') -> str:
    """
    Align a float number according to the sides widths. The purpose is
    to send various float numbers to align them by the points.
    The number must always have a decimal point.
    
    Examples::

        fljust('1.23', [3, 5], '-')   
        fljust('1.2', [3, 5], '-')    
        fljust('.00321', [3, 5], '-')
        
    Results in::
    
        '--1.23---'
        '--1.2----'
        '---.00321'
    """
    # If the string is a float, it should have a point, 
    # si it gets splitted by that point. 
    splitted = string.split('.') #FIX add try/except
    
    # Take the left side and the right side, and its widths.
    left_string = splitted[LEFT_SIDE_I]
    right_string = splitted[RIGHT_SIDE_I]
    left_width = sides_widths[LEFT_SIDE_WIDTH_I]
    right_width = sides_widths[RIGHT_SIDE_WIDTH_I]
    
    # Align the left part to the right.
    left = left_string.rjust(left_width, fill_char) 
    
    # Align the right part to the left.
    right = right_string.ljust(right_width, fill_char)
    
    return '.'.join([left, right])


def __fljust_part(cell_part: Any, 
                  cell_length: int, 
                  float_column_sizes: Union[List[int], Tuple[int, int, int]], 
                  fill_char: str = ' '
                 ) -> str:
    """
    This will align a cell part.
    If it has a point, it will be aligned as a float with ``fljust()``.
    Int numbers are also aligned with the int part of the floats, but
    using ``_add_cell_spacing()``.
    Any other element (nor float nor int) is aligned with ``str().rjust()``
    
    Examples::

        __fljust_part('1.23', 9, [3, 1, 5], '-')   
        __fljust_part('1.2', 9, [3, 1, 5], '-')    
        __fljust_part('.00321', 9, [3, 1, 5], '-') 
        __fljust_part('5', 9, [3, 1, 5], '-')      
        __fljust_part('?', 9, [3, 1, 5], '-')
        
    Results in::
    
        '--1.23---'
        '--1.2----'
        '---.00321'
        '--5------'
        '--------?'      
    
    """
    # Convert to string because anything could come. 
    str_cell = str(cell_part) 
    
    # Check if the cell part is a float or an int.
    is_float_number = FLT_FILTER(
        str_cell
    ) is not None
    is_int_number = INT_FILTER(
        str_cell
    ) is not None
    
    # If it is a float, align it as a float.
    if is_float_number:
        return fljust(
            str_cell, 
            float_column_sizes, 
            fill_char
        )
    
    # If it is an int, align it as an int.
    # Will be aligned to the int part of the float.
    if is_int_number:
        cell_len = len(str_cell)
        
        # Get the left and right sides widths, subtracting
        # the length of the int part to the left and adding
        # the len of the point to the right.
        #
        # Explanation:
        # '--1.2----'   Having these floats aligned.
        # '---.00321'   
        # '--5------'   If an int is going to be aligned with the same sizes:
        #  ---              left width of 3
        #     -             dot width of 1
        #      ------       right width of 5
        #               Will do the following:
        #  --               1. Subtract its width of the left.
        #     -------       2. Adding the width of the dot to the right.
        #  --5-------       3. add those two spaces to the left and right.
        
        # Get the left and right sides widths.
        left_width = float_column_sizes[LEFT_SIDE_WIDTH_I]
        right_width = float_column_sizes[RIGHT_SIDE_WIDTH_I]
        
        # Subtract the length of the int part to the left.
        fixed_left_width = left_width - cell_len
        
        # Add the len of the point to the right.
        fixed_right_width = right_width + float_column_sizes[POINT_WIDTH_I]
        
        # Add the spaces to the left and right.
        return _add_cell_spacing(
            str_cell,
            fixed_left_width,
            fixed_right_width,
            0,
            fill_char
        )
        
    # If it is not a float nor an int, align it to the right.
    else:
        return str_cell.rjust(
            cell_length, fill_char
        )


def _fljust_cell(cell: Union[str, Union[List[str], Tuple[str]]], 
                 cell_length: int, 
                 float_column_sizes: Union[List[int], Tuple[int, int, int]],
                 fill_char: str = ' ', 
                 ) -> Union[str, Union[List[str], Tuple[str]]]:
    """
    Examples::
        
        _fljust_cell('1.23', 9, [3, 1, 5], '-')               
        _fljust_cell('1.2', 9, [3, 1, 5], '-')                
        _fljust_cell('.00321', 9, [3, 1, 5], '-')             
        _fljust_cell('5', 9, [3, 1, 5], '-')                  
        _fljust_cell(['Nothing', 'here'], 9, [3, 1, 5], '-')

    will result in::
        
        '--1.23---'
        '--1.2----'
        '---.00321'
        '--5------'
        ('--Nothing', 
         '-----here') 
  
    """
    # If it is a wrapped cell (list or tuple), align each part.
    if is_some_instance(cell, list, tuple):
        float_adjusted = list(map(str, cell))  # Convert to string.
        for part_i, cell_part in enumerate(float_adjusted):
            float_adjusted[part_i] = __fljust_part(
                cell_part,
                cell_length,
                float_column_sizes,
                fill_char
            )
        float_adjusted = tuple(float_adjusted)
        
    # If it is not a wrapped cell, align it.
    else:
        float_adjusted = __fljust_part(
            cell,
            cell_length,
            float_column_sizes,
            fill_char
        )
            
    return float_adjusted


def _zip_wrapped_rows(wrapped_headers: Union[list, tuple], 
                      wrapped_rows: Union[list, tuple]
                     ) -> Tuple[tuple, tuple]:
    """
    Will zip a wrapped row and convert it to a wrapped column.
    
    A wrapped row looks like this::

    [['Wrapped', 'Looking']['row', 'good']]
    
    In order to put in a column, it needs to be paired with
    it's respective part of the consequent sub-rows, so 0
    goes with 0, 1 goes with 1, 2 goes with 2, etc.

    >>>    0          1          0      1
    >>> [['Wrapped', 'Looking']['row', 'good']]
    
    The zip function does exactly that::

        tuple(zip(*[['Wrapped', 'Looking']['row', 'good']]))
    
    results in::

        (('Wrapped', 'row'), ('Looking', 'good'))
    
    But it's also necessary to consider that the intention is to 
    convert a row in a column, so the process must be done twice:
    one for the wrapped cells, and one for all the rows::
    
        _zip_wrapped_rows([
            [['Data'   , 'In a row']],   # Not wrapped.
            [['Wrapped', 'Looking']      # Wrapped.
            ['row'    , 'good'   ]],
            [['More'   , 'data'   ]],    # Not wrapped.
        ])              
                        
    results in::

        (
            ('Data', ('Wrapped', 'row'), 'More'),
            ('In a row', ('Looking', 'good'), 'data'),
        )
    """
    zipped_wrapped_cells = []
    for column_i, column in enumerate(wrapped_rows):
        # If there's any wrapped cells, here is where they are zipped.
        zipped_wrapped_cells.append(__zip_sub_rows(column))
    # Now, the rows are zipped to be converted to columns.
    zipped_rows = tuple(zip(*zipped_wrapped_cells))
    # The headers are zipped to be converted to columns (in case
    # of a wrapped header).
    zipped_headers = __zip_sub_rows(wrapped_headers)

    return zipped_rows, zipped_headers


def __zip_sub_rows(row: Union[list, tuple]) -> tuple:
    """
    Zips a wrapped row::

        __zip_sub_rows([['a', 'b'], ['c', 'd']]) -> (('a', 'c'), ('b', 'd'))
        __zip_sub_rows([['a', 'b']]) -> ('a', 'b')
    """
    if len(row) > 1:
        # If there's more than one sub-row, zip them.
        zipped_sub_rows = tuple(zip(*row))
        return zipped_sub_rows
    else:
        # If there's only one sub-row, return it.
        only_sub_row = row[0]
        return only_sub_row

def _wrap_rows(headers: Union[list, tuple], 
               data: Union[List[Union[list, tuple]], Tuple[Union[list, tuple]]]
              ) -> Tuple[list, list]:
    """
    Wraps the rows and headers of the table if
    any new line characters are present::

        _wrap_rows(headers=['a', 'b\\nc'], data=[['a', 'b\\nc'], ['c', 'd']])
    
    Results in:

    >>> ([['a', 'b'], ['', 'c']], [[['a', 'b'], ['', 'c']], [['c', 'd']]])
    >>>  |    ^          ^     |  |    ^          ^     |  |          |
    >>> #  sub-row    sub-row       sub-row    sub-row      no sub-rows
    >>> #<-------wrapped------->  <-------wrapped------->  <not wrapped>
    """
    # If no headers are provided, return None.
    wrapped_headers = None
    
    there_are_headers = headers is not None and is_some_instance(headers, list, tuple)
    if there_are_headers:
        # If there are headers, wrap them.
        wrapped_headers = __wrap_single_row(headers)
        
    # Wrap each row.
    # If no new line characters are present, data is returned as it is.
    wrapped_data = list(map(__wrap_single_row, data))

    return wrapped_headers, wrapped_data


def __wrap_single_row(row: Union[list, tuple]) -> list:
    """
    Will split every cell that has an new line character.
    The splitted cell generates a new sub-row, and every other
    cell that doesn't have a new line character will be adjusted::

        __wrap_single_row(['a', 'b\\nc'])
    
    Results in:
    
    >>> [['a', 'b'], ['', 'c']]
    >>>                ^
    >>> # Blank space to adjust the cell.
    """
    # Split in lines if any new line characters are present.
    splitted_cells = list(map(__wrap_cell, row))
    
    # Get the quantity of sub-rows calculating the max length of 
    # all of the splitted (or not) cells.
    quantity_of_sub_rows = max([len(x) for x in splitted_cells])
    
    # Create blank sub-rows each one having the same quantity of 
    # cells as the original row.
    sub_rows = [['' for x in range(len(row))] 
                for _ in range(quantity_of_sub_rows)]
    
    # Fill the sub-rows with the splitted cells.
    # 
    # [['a'], ['b', 'c']]       <-- splitted_cells
    #    ^      ^    ^
    #  sbr0   sbr0  sbr1
    # <cell0> <--cell1-->
    #  
    # [['a', 'b'], ['', 'c']]   <-- sub_rows (being filled)
    #    ^    ^     ^    ^
    # [0][0] [0][1] ^  [1][1]   <-- sub_rows[sub_row][cell]
    # [0][0] [1][0] ^  [1][1]   <-- splitted_cells[cell][sub-row]  
    #               ^
    #   There's no second sub-row in the first cell,
    #   so it's just left empty
    # 
    for cell in range(len(splitted_cells)):
        for sub_row in range(len(splitted_cells[cell])):
            sub_rows[sub_row][cell] = splitted_cells[cell][sub_row]

    return sub_rows


def __wrap_cell(cell: Any) -> Union[List[str], Any]: 
    """
    Split in lines a cell if it has a new line character::
    
        'a' -> ['a']
        'a\\nb' -> ['a', 'b']
        '' -> ['']
        123 -> [123]
        None -> [None]
    """
    # Only if the cell is a string.
    if isinstance(cell, str):
        if cell != '':
            # If the cell is not empty,
            # apply the str method splitlines
            return cell.splitlines()
        else:
            # Return a list with empty string in case of empty cell.
            return ['']
    else:
        # If the cell is not a string, return it as it is.
        return [cell]


if __name__ == '__main__':
    print('This shouldn\'t be printing.')
