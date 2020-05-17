from objects.datatypeConsts import str_t, bool_t
from objects.parseObject import Widget

SEP_VALID = [
    ('takeFocus', bool_t),
    ('orient', str_t)
]

SEP_REC = [
    'orient'
]


class Separator(Widget):
    def __init__(self, name):
        super().__init__(name, SEP_VALID, SEP_REC)
