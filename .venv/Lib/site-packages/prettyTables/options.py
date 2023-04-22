"""
OPTIONS

some parameters for the creation of styles,
formatting, and other things.
"""

import re


# +-------------------------+ CONSTANTS +------------------------+

# For styles without vertical lines.
INVISIBLE_SEPARATOR = ' '
# Default value for an empty cell.
NONE_VALUE_REPLACEMENT = ''
# Default value to fill cells when aligning.
DEFAULT_FILL_CHAR = ' '
# The style is set if the user doesn't choose or puts an incorrect value.
DEFAULT_STYLE = 'grid_eheader'
# Default index column header.
I_COL_TIT = 'i'
# Default space a cell has on each side (after aligning).
CELL_MARGIN = 1
# Not used yet.
DEFAULT_TABLE_ALIGNMENT = 'l'
# Default string that is shown when a cell is trimmed.
DEFAULT_TRIMMING_SIGN = '...'
# How small can a column be.
MIN_COLUMN_SIZE = 3


# +--------------------------+ REGEX +---------------------------+

# To find integer numbers.
INT_FILTER = re.compile(r'^[-]?[0-9]*$').match
# TO find float numbers (not exponential ones)
FLT_FILTER = re.compile(r'^[-]?[0-9]*[.][0-9]*$').match


# +--------------------------------------------------------------+
