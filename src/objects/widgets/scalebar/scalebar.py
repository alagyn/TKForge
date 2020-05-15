from objects.datatypeConsts import str_t, float_t, name_t, func_t, bool_t, int_t
from objects.parseObject import Widget

SCALEBAR_VALID = [
    ('takeFocus', bool_t),
    ('bottomValue', float_t),
    ('topValue', float_t),
    ('command', func_t),
    ('variable', name_t),
    ('orient', str_t),
    ('length', int_t),
    ('defaultValue', float_t)
]

SCALEBAR_REC = [
    'variable', 'orient', 'bottomValue', 'topValue'
]


class Scalebar(Widget):
    def __init__(self, name):
        super().__init__(name, SCALEBAR_VALID, SCALEBAR_REC)

