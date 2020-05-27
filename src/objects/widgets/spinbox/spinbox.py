from objects.datatypeConsts import float_t, bool_t, strList_t, str_t, name_t
from objects.parseObject import Widget

SPINBOX_PARAM = [
    ('takeFocus', 'takefocus', bool_t),
    ('validateMode', 'validate', str_t),
    ('format', 'format', str_t),
    ('bottomVal', 'from', float_t),
    ('topVal', 'to', float_t),
    ('values', 'values', strList_t),
    ('wrap', 'wrap', bool_t),
    ('incrementVal', 'increment', float_t)
]

OTHER = [
    ('command', '', bool_t),
    ('xScroll', '', name_t),
    ('validate', '', bool_t),
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
        super().__init__(name, SPINBOX_PARAM + OTHER, SPINBOX_REC)

