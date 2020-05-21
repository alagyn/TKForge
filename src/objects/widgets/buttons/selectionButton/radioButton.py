from objects.datatypeConsts import name_t, str_t, bool_t, int_t
from objects.parseObject import Widget

RADIO_V = [
    ('takeFocus', 'takefocus', bool_t),
    ('text', 'text', str_t),
    ('textVariable', 'textvariable', name_t),
    ('acceleratorIdx', 'underline', int_t),
    ('width', 'width', int_t),
    ('onValue', 'onvalue', str_t),
    ('outputVariable', 'variable', name_t),

]

COMMAND = [
    ('command', '', bool_t)
]

RADIO_REC = [
    'onValue', 'outputVariable'
]


class RadioButton(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, RADIO_V + COMMAND, RADIO_REC)
