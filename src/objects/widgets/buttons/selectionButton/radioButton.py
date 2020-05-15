from objects.datatypeConsts import name_t, str_t
from objects.parseObject import Widget

RADIO_V = [
    ('onValue', str_t),
    ('outputVariable', name_t)
]

RADIO_REC = [
    'onValue', 'outputVariable'
]


class RadioButton(Widget):
    def __init__(self, name):
        super().__init__(name, RADIO_V, RADIO_REC)

# TOFIX Radiobutton