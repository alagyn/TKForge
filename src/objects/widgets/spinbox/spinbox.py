from objects.datatypeConsts import float_t, bool_t, strList_t, str_t, name_t, int_t
from objects.parseObject import Widget

SPINBOX_PARAM = [
    ('takeFocus', bool_t),
    ('command', bool_t),
    ('xScroll', name_t),
    ('validateMode', str_t),
    ('validate', bool_t),
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
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, SPINBOX_PARAM, SPINBOX_REC)

