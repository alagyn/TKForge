from ..parseObject import Widget, Style
from ...buildConsts import bool_t, color_t, name_t, func_t, str_t, int_t, float_t, strList_t, intList_t
from ...buildConsts import active_s, disabled_s, focus_s, readonly_s

SPINBOX_PARAM = [
    ('takeFocus', bool_t),
    ('command', func_t),
    ('xScroll', name_t),
    ('validateMode', str_t),
    ('validateCommmand', func_t),
    ('width', int_t),
    ('formatting', str_t),
    ('bottomVal', float_t),
    ('topVal', float_t),
    ('values', strList_t),
    ('wrap', bool_t),
    ('incrementVal', float_t)
]

SPINBOX_REC = [
    'bottomVal', 'topVal', 'incrementVal'
]


class Spinbox(Widget):
    def __init__(self, name):
        super().__init__(name, SPINBOX_PARAM, SPINBOX_REC)


SPINBOX_STYLE = [
    ('arrowColor', color_t),
    ('arrowSize', int_t),
    ('background', color_t),  # Internal fieldbackground
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('textColor', color_t),
    ('lightColor', color_t),
    ('padding', intList_t),
    ('selectedBG', color_t),
    ('selectedTextColor', color_t)
]

SPINBOX_STATES = [
    active_s, disabled_s, focus_s, readonly_s
]


class SpinboxStyle(Style):
    def __init__(self, name):
        super().__init__(name, SPINBOX_STYLE, SPINBOX_STATES)
