# Entry
from objects.datatypeConsts import name_t, str_t, bool_t, int_t
from objects.parseObject import Widget

ENTRY_VALID = [
    ('takeFocus', 'takefocus', bool_t),
    ('justify', 'justify', str_t),
    ('passwordChar', 'show', str_t),
    ('defaultState', 'state', str_t),
    ('outputVariable', 'textvariable', name_t),
    ('width', 'width', int_t),
    ('validateMode', 'validate', str_t)
]

VALIDATE = [
    ('validate', '', bool_t)
]

SCROLL = [
    ('xScroll', '', name_t)
]

ENTRY_REC = [
    # Intentionally left blanl
]


class Entry(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, ENTRY_VALID + SCROLL + VALIDATE, ENTRY_REC)
