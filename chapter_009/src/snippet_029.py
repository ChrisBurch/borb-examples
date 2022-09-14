# new imports
from borb.pdf import TableCell


def empty_cell_without_borders():
    return TableCell(
        Paragraph(" "),
        border_top=False,
        border_right=False,
        border_bottom=False,
        border_left=False,
    )
