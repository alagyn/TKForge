# Entry
from objects.datatypeConsts import name_t, func_t, str_t, bool_t, int_t
from objects.parseObject import Widget

ENTRY_VALID = [
    ('takeFocus', bool_t),
    ('justify', str_t),
    ('passwordChar', str_t),
    ('defaultState', str_t),
    ('outputVariable', name_t),
    ('width', int_t),
    ('validateMode', str_t),
    ('validateCommand', func_t),
    ('xScroll', name_t)
]

ENTRY_REC = [
    # Intentionally left blanl
]


class Entry(Widget):
    def __init__(self, name):
        super().__init__(name, ENTRY_VALID, ENTRY_REC)