from objects.datatypeConsts import float_t, bool_t, strList_t, str_t, func_t, name_t, int_t
from objects.parseObject import Widget

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

