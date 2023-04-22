"""
COMPOSITION SETS - STYLES

A composition set is a named tuple which contain the characters
for each part of the table. Here are are the ones currently added.

*This part was based (mainly) in the "tabulate" package structure!
"""

from collections import namedtuple

from .options import INVISIBLE_SEPARATOR, CELL_MARGIN

TableComposition = namedtuple(
    'TableComposition',
    [
        'superior_header_line',
        'inferior_header_line',
        'superior_header_line_no_header',
        'table_body_line',
        'table_end_line',
        'vertical_header_lines',
        'vertical_table_body_lines',
        'margin',
        'align_sensitive',
        'align_indicator',
        'centered_indicator_on_sides'
    ]
)

HorizontalComposition = namedtuple(
    'HorizontalComposition',
    [
        'superior_header_line',
        'inferior_header_line',
        'superior_header_line_no_header',
        'table_body_line',
        'table_end_line'
    ]
)

SeparatorLine = namedtuple(
    'SeparatorLine',
    [
        'left',
        'middle',
        'intersection',
        'right'
    ]
)

AlignIndicator = namedtuple(
    'AlignIndicator',
    [
        'sides',
        'center'
    ]
)

Compositions = namedtuple(
    'Compositions',
    [
        'plain',

        # Box drawing Tables
        'pretty_grid',
        'pretty_columns',
        'bold_header',
        'bheader_columns',
        'bold_eheader',
        'beheader_columns',
        'bheader_ebody',
        'round_edges',
        're_eheader',
        're_ebody',
        # Thin borderline
        'thin_borderline',
        'th_bd_eheader',
        'th_bd_ebody',
        'th_bd_empty',
        # Bold Borderline
        'bold_borderline',
        'bd_bl_eheader',
        'bd_bl_ebody',
        'bd_bl_empty',

        # +-|~oO:
        'pwrshll_alike',
        'presto',
        'grid',
        'grid_eheader',
        'grid_ebody',
        'grid_empty',
        'pipes',
        'tilde_grid',
        'tilg_eheader',
        'tilg_columns',
        'tilg_empty',
        'orgtbl',

        # Simple (horizontal lines)
        'clean',
        'simple',
        'simple_bold',
        'simple_head',
        'simple_head_bold',
        'sim_th_bl',
        'sim_bd_bl',
        'sim_head_th_bl',
        'sim_head_bd_bl',

        # Other
        'dashes'
    ]
)

__style_compositions = Compositions(
    plain=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=0,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),

    ###################################
    ####     Box drawing Tables    ####
    ###################################
    pretty_grid=TableComposition(
        superior_header_line=SeparatorLine('╒', '═', '╤', '╕'),
        inferior_header_line=SeparatorLine('╞', '═', '╪', '╡'),
        superior_header_line_no_header=SeparatorLine('╒', '═', '╤', '╕'),
        table_body_line=SeparatorLine('├', '─', '┼', '┤'),
        table_end_line=SeparatorLine('╘', '═', '╧', '╛'),
        vertical_header_lines=SeparatorLine('│', '│', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    pretty_columns=TableComposition(
        superior_header_line=SeparatorLine('╒', '═', '╤', '╕'),
        inferior_header_line=SeparatorLine('╞', '═', '╪', '╡'),
        superior_header_line_no_header=SeparatorLine('╒', '═', '╤', '╕'),
        table_body_line=None,
        table_end_line=SeparatorLine('╘', '═', '╧', '╛'),
        vertical_header_lines=SeparatorLine('│', '│', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bold_header=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '╦', '╗'),
        inferior_header_line=SeparatorLine('╚', '═', '╩', '╝'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=SeparatorLine('├', '─', '┼', '┤'),
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('║', '║', None, '║'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bheader_columns=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '╦', '╗'),
        inferior_header_line=SeparatorLine('╚', '═', '╩', '╝'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('║', '║', None, '║'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bold_eheader=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '═', '╗'),
        inferior_header_line=SeparatorLine('╚', '═', '═', '╝'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=SeparatorLine('├', '─', '┼', '┤'),
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('║', ' ', None, '║'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    beheader_columns=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '═', '╗'),
        inferior_header_line=SeparatorLine('╚', '═', '═', '╝'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('║', ' ', None, '║'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bheader_ebody=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '═', '╗'),
        inferior_header_line=SeparatorLine('╚', '═', '═', '╝'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '─', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '─', '─', '┘'),
        vertical_header_lines=SeparatorLine('║', ' ', None, '║'),
        vertical_table_body_lines=SeparatorLine('│', ' ', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    round_edges=TableComposition(
        superior_header_line=SeparatorLine('╭', '─', '┬', '╮'),
        inferior_header_line=SeparatorLine('╞', '═', '╪', '╡'),
        superior_header_line_no_header=SeparatorLine('╭', '─', '┬', '╮'),
        table_body_line=None,
        table_end_line=SeparatorLine('╰', '─', '┴', '╯'),
        vertical_header_lines=SeparatorLine('│', '│', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    re_eheader=TableComposition(
        superior_header_line=SeparatorLine('╭', '─', '─', '╮'),
        inferior_header_line=SeparatorLine('╞', '═', '╤', '╡'),
        superior_header_line_no_header=SeparatorLine('╭', '─', '┬', '╮'),
        table_body_line=None,
        table_end_line=SeparatorLine('╰', '─', '┴', '╯'),
        vertical_header_lines=SeparatorLine('│', ' ', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    re_ebody=TableComposition(
        superior_header_line=SeparatorLine('╭', '─', '─', '╮'),
        inferior_header_line=SeparatorLine('╞', '═', '═', '╡'),
        superior_header_line_no_header=SeparatorLine('╭', '─', '─', '╮'),
        table_body_line=None,
        table_end_line=SeparatorLine('╰', '─', '─', '╯'),
        vertical_header_lines=SeparatorLine('│', ' ', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', ' ', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    ###########################
    ####  Thin borderline  ####
    ###########################
    thin_borderline=TableComposition(
        superior_header_line=SeparatorLine('┌', '─', '┬', '┐'),
        inferior_header_line=SeparatorLine('╞', '═', '╪', '╡'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=SeparatorLine('├', '─', '┼', '┤'),
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('│', '│', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    th_bd_eheader=TableComposition(
        superior_header_line=SeparatorLine('┌', '─', '─', '┐'),
        inferior_header_line=SeparatorLine('╞', '═', '╤', '╡'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '┬', '┐'),
        table_body_line=SeparatorLine('├', '─', '┼', '┤'),
        table_end_line=SeparatorLine('└', '─', '┴', '┘'),
        vertical_header_lines=SeparatorLine('│', ' ', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', '│', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    th_bd_ebody=TableComposition(
        superior_header_line=SeparatorLine('┌', '─', '┬', '┐'),
        inferior_header_line=SeparatorLine('╞', '═', '╧', '╡'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '─', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '─', '─', '┘'),
        vertical_header_lines=SeparatorLine('│', '│', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', ' ', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    th_bd_empty=TableComposition(
        superior_header_line=SeparatorLine('┌', '─', '─', '┐'),
        inferior_header_line=SeparatorLine('╞', '═', '═', '╡'),
        superior_header_line_no_header=SeparatorLine('┌', '─', '─', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '─', '─', '┘'),
        vertical_header_lines=SeparatorLine('│', ' ', None, '│'),
        vertical_table_body_lines=SeparatorLine('│', ' ', None, '│'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    ###########################
    ####  Bold borderline  ####
    ###########################
    bold_borderline=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '╤', '╗'),
        inferior_header_line=SeparatorLine('╠', '═', '╪', '╣'),
        superior_header_line_no_header=SeparatorLine('╔', '═', '╤', '╗'),
        table_body_line=SeparatorLine('╟', '─', '┼', '╢'),
        table_end_line=SeparatorLine('╚', '═', '╧', '╝'),
        vertical_header_lines=SeparatorLine('║', '│', None, '║'),
        vertical_table_body_lines=SeparatorLine('║', '│', None, '║'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bd_bl_eheader=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '═', '╗'),
        inferior_header_line=SeparatorLine('╠', '═', '╤', '╣'),
        superior_header_line_no_header=SeparatorLine('╔', '═', '╤', '╗'),
        table_body_line=SeparatorLine('╟', '─', '┼', '╢'),
        table_end_line=SeparatorLine('╚', '═', '╧', '╝'),
        vertical_header_lines=SeparatorLine('║', ' ', None, '║'),
        vertical_table_body_lines=SeparatorLine('║', '│', None, '║'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bd_bl_ebody=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '╤', '╗'),
        inferior_header_line=SeparatorLine('╠', '═', '╧', '╣'),
        superior_header_line_no_header=SeparatorLine('╔', '═', '═', '╗'),
        table_body_line=None,
        table_end_line=SeparatorLine('╚', '═', '═', '╝'),
        vertical_header_lines=SeparatorLine('║', '│', None, '║'),
        vertical_table_body_lines=SeparatorLine('║', ' ', None, '║'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    bd_bl_empty=TableComposition(
        superior_header_line=SeparatorLine('╔', '═', '═', '╗'),
        inferior_header_line=SeparatorLine('╠', '═', '═', '╣'),
        superior_header_line_no_header=SeparatorLine('╔', '═', '═', '╗'),
        table_body_line=None,
        table_end_line=SeparatorLine('╚', '═', '═', '╝'),
        vertical_header_lines=SeparatorLine('║', ' ', None, '║'),
        vertical_table_body_lines=SeparatorLine('║', ' ', None, '║'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),

    ###########################
    ####      +-|~oO:      ####
    ###########################
    pwrshll_alike=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '-', ' ', None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, ' ', None, None),
        vertical_table_body_lines=SeparatorLine(None, ' ', None, None),
        margin=0,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    presto=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '-', '+', None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, '|', None, None),
        vertical_table_body_lines=SeparatorLine(None, '|', None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    grid=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '+', '+'),
        inferior_header_line=SeparatorLine('+', '=', '+', '+'),
        superior_header_line_no_header=SeparatorLine('+', '-', '+', '+'),
        table_body_line=SeparatorLine('+', '-', '+', '+'),
        table_end_line=SeparatorLine('+', '-', '+', '+'),
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    grid_eheader=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '-', '+'),
        inferior_header_line=SeparatorLine('+', '=', '+', '+'),
        superior_header_line_no_header=SeparatorLine('+', '-', '+', '+'),
        table_body_line=None,
        table_end_line=SeparatorLine('+', '-', '+', '+'),
        vertical_header_lines=SeparatorLine('|', ' ', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    grid_ebody=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '+', '+'),
        inferior_header_line=SeparatorLine('+', '=', '+', '+'),
        superior_header_line_no_header=SeparatorLine('+', '-', '-', '+'),
        table_body_line=None,
        table_end_line=SeparatorLine('+', '-', '-', '+'),
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', ' ', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    grid_empty=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '-', '+'),
        inferior_header_line=SeparatorLine('+', '=', '=', '+'),
        superior_header_line_no_header=SeparatorLine('+', '-', '-', '+'),
        table_body_line=None,
        table_end_line=SeparatorLine('+', '-', '-', '+'),
        vertical_header_lines=SeparatorLine('|', ' ', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', ' ', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    pipes=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine('|', '-', '|', '|'),
        superior_header_line_no_header=SeparatorLine('|', '-', '|', '|'),
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=True,
        align_indicator=AlignIndicator(':', ':'),
        centered_indicator_on_sides=True
    ),
    tilde_grid=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '+', '+'),
        inferior_header_line=SeparatorLine('O', '~', 'O', 'O'),
        superior_header_line_no_header=SeparatorLine('O', '~', 'O', 'O'),
        table_body_line=SeparatorLine('+', '-', '+', '+'),
        table_end_line=SeparatorLine('O', '~', 'O', 'O'),
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    tilg_eheader=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '-', '+'),
        inferior_header_line=SeparatorLine('O', '~', 'O', 'O'),
        superior_header_line_no_header=SeparatorLine('O', '~', 'O', 'O'),
        table_body_line=SeparatorLine('+', '-', '+', '+'),
        table_end_line=SeparatorLine('O', '~', 'O', 'O'),
        vertical_header_lines=SeparatorLine('|', ' ', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    tilg_columns=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '+', '+'),
        inferior_header_line=SeparatorLine('O', '~', 'O', 'O'),
        superior_header_line_no_header=SeparatorLine('O', '~', 'O', 'O'),
        table_body_line=None,
        table_end_line=SeparatorLine('O', '~', 'O', 'O'),
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    tilg_empty=TableComposition(
        superior_header_line=SeparatorLine('+', '-', '-', '+'),
        inferior_header_line=SeparatorLine('O', '~', '~', 'O'),
        superior_header_line_no_header=SeparatorLine('O', '~', '~', 'O'),
        table_body_line=None,
        table_end_line=SeparatorLine('O', '~', '~', 'O'),
        vertical_header_lines=SeparatorLine('|', ' ', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', ' ', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    orgtbl=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine('|', '-', '+', '|'),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine('|', '|', None, '|'),
        vertical_table_body_lines=SeparatorLine('|', '|', None, '|'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),

    ###################################
    #### Simple (horizontal lines) ####
    ###################################
    clean=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '─', INVISIBLE_SEPARATOR, None),
        superior_header_line_no_header=SeparatorLine(None, '─', INVISIBLE_SEPARATOR, None),
        table_body_line=None,
        table_end_line=SeparatorLine(None, '─', INVISIBLE_SEPARATOR, None),
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=0,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    simple=TableComposition(
        superior_header_line=SeparatorLine(None, '-', '-' * len(INVISIBLE_SEPARATOR), None),
        inferior_header_line=SeparatorLine(None, '-', '-' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=SeparatorLine(None, '-', '-' * len(INVISIBLE_SEPARATOR), None),
        table_body_line=None,
        table_end_line=SeparatorLine(None, '-', '-' * len(INVISIBLE_SEPARATOR), None),
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    simple_bold=TableComposition(
        superior_header_line=SeparatorLine(None, '=', '=' * len(INVISIBLE_SEPARATOR), None),
        inferior_header_line=SeparatorLine(None, '=', '=' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=SeparatorLine(None, '=', '=' * len(INVISIBLE_SEPARATOR), None),
        table_body_line=None,
        table_end_line=SeparatorLine(None, '=', '=' * len(INVISIBLE_SEPARATOR), None),
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    simple_head=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '-', '-' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    simple_head_bold=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '=', '=' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    sim_th_bl=TableComposition(
        superior_header_line=SeparatorLine(None, '─', '─' * len(INVISIBLE_SEPARATOR), None),
        inferior_header_line=SeparatorLine(None, '─', '─' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=SeparatorLine(None, '─', '─' * len(INVISIBLE_SEPARATOR), None),
        table_body_line=None,
        table_end_line=SeparatorLine(None, '─', '─' * len(INVISIBLE_SEPARATOR), None),
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    sim_bd_bl=TableComposition(
        superior_header_line=SeparatorLine(None, '═', '═' * len(INVISIBLE_SEPARATOR), None),
        inferior_header_line=SeparatorLine(None, '═', '═' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=SeparatorLine(None, '═', '═' * len(INVISIBLE_SEPARATOR), None),
        table_body_line=None,
        table_end_line=SeparatorLine(None, '═', '═' * len(INVISIBLE_SEPARATOR), None),
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    sim_head_th_bl=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '─', '─' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    sim_head_bd_bl=TableComposition(
        superior_header_line=None,
        inferior_header_line=SeparatorLine(None, '═', '═' * len(INVISIBLE_SEPARATOR), None),
        superior_header_line_no_header=None,
        table_body_line=None,
        table_end_line=None,
        vertical_header_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        vertical_table_body_lines=SeparatorLine(None, INVISIBLE_SEPARATOR, None, None),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    ),
    ##################
    ####   Other  ####
    ##################
    dashes=TableComposition(
        superior_header_line=SeparatorLine('┌', '┄', '┬', '┐'),
        inferior_header_line=SeparatorLine('┝', '╍', '┿', '┥'),
        superior_header_line_no_header=SeparatorLine('┌', '┄', '┬', '┐'),
        table_body_line=None,
        table_end_line=SeparatorLine('└', '┄', '┴', '┘'),
        vertical_header_lines=SeparatorLine('┊', '┊', None, '┊'),
        vertical_table_body_lines=SeparatorLine('┊', '┊', None, '┊'),
        margin=CELL_MARGIN,
        align_sensitive=False,
        align_indicator=None,
        centered_indicator_on_sides=False
    )
)
