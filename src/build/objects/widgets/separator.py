from ..parseObject import Widget, Style
from ...buildConsts import bool_t, str_t, color_t

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


SEP_STYLE_PARAM = [
    ('background', color_t)
]


class SeparatorStyle(Style):
    def __init__(self, name):
        super().__init__(name, SEP_STYLE_PARAM, [])
