from objects.datatypeConsts import name_t, str_t, bool_t, int_t
from objects.parseObject import Widget

RADIO_V = [
    ('image', str_t),
    ('takeFocus', bool_t),
    ('text', str_t),
    ('textVariable', name_t),
    ('underline', int_t),  # TODO RadioBtn accellerator
    ('width', int_t),
    ('command', bool_t),
    ('onValue', str_t),
    ('outputVariable', name_t)
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
        super().__init__(name, RADIO_V, RADIO_REC)
