from ..parseObject import ParseObject
from typing import List, Tuple

from ...buildConsts import str_t, bool_t, intList_t, int_t, name_t, color_t

# Textbox
TEXTBOX_VALID = [
    ('highlightWidth', int_t),
    ('hightlightUnselected', color_t),
    ('highlightSelected', color_t),
    ('xScroll', name_t),
    ('yScroll', name_t),
    ('selectBG', color_t),
    ('selectTextColor', color_t),
    ('selectBorderWidth', int_t),
    ('state', str_t),
    ('wrap', str_t),
    ('tabStyle', str_t),
    ('undo', bool_t),
    ('maxUndo', int_t),
    ('aboveLineSpace', int_t),
    ('betweenWrapSpace', int_t),
    ('belowLineSpace', int_t),
    ('text', str_t),
    ('editable', bool_t),
    ('font', str_t),
    ('padding', intList_t),
    ('relief', str_t),
    ('defaultBackColor', color_t),
    ('textColor', color_t)

]

TEXTBOX_REQ = [
    # Intentionally left blank
]


class TextBox(ParseObject):
    def __init__(self, name):
        super().__init__(name, TEXTBOX_VALID, TEXTBOX_REQ)
