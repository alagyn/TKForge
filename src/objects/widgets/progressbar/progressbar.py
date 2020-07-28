from objects.datatypeConsts import bool_t, str_t, int_t, name_t, float_t
from objects.parseObject import Widget

PROGRESS_BAR_VALID = [
    ('takeFocus', 'takefocus', bool_t),
    ('type', 'mode', str_t),
    ('length', 'length', int_t),
    ('inputVariable', 'variable', name_t),
    ('maximum', 'maximum', float_t),
    ('startValue', 'value', float_t),
    ('orient', 'orient', str_t)
]

PROGRESS_BAR_REC = [
    'type', 'orient'
]


class Progressbar(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, PROGRESS_BAR_VALID, PROGRESS_BAR_REC)
