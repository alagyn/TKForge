from objects.datatypeConsts import str_t, float_t, name_t, bool_t, int_t
from objects.parseObject import Widget

SCALEBAR_VALID = [
    ('takeFocus', 'takefocus', bool_t),
    ('bottomValue', 'from', float_t),
    ('topValue', 'to', float_t),
    ('variable', 'variable', name_t),
    ('orient', 'orient', str_t),
    ('length', 'length', int_t),
    ('defaultValue', 'value', float_t)
]

SCALEBAR_REC = [
    'variable', 'orient', 'bottomValue', 'topValue'
]


class Scalebar(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, SCALEBAR_VALID, SCALEBAR_REC)
