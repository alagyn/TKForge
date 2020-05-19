from objects.datatypeConsts import bool_t, str_t, int_t, name_t, float_t
from objects.parseObject import Widget

PROGRESS_BAR_VALID = [
    ('takeFocus', bool_t),
    ('type', str_t),
    ('length', int_t),
    ('inputVariable', name_t),
    ('maximum', float_t),
    ('startValue', float_t),
    ('orient', str_t)
]

PROGRESS_BAR_REC = [
    'type', 'orient'
]


class Progressbar(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, PROGRESS_BAR_VALID, PROGRESS_BAR_REC)
