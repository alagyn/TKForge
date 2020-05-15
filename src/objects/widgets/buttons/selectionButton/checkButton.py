from objects.datatypeConsts import str_t, name_t
from objects.parseObject import Widget

CHECK_V = [
    ('onValue', str_t),
    ('offValue', str_t),
    ('outputVariable', name_t)
]

CHECK_REC = [
    'onValue', 'offValue', 'outputVariable'
]


class CheckButton(Widget):
    def __init__(self, name):
        super().__init__(name, CHECK_V, CHECK_REC)

# TOFIX Checkbutton