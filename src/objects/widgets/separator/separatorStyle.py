from objects.datatypeConsts import color_t
from objects.parseObject import Style

SEP_STYLE_PARAM = [
    ('background', 'background', color_t)
]


class SeparatorStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SEP_STYLE_PARAM, [])
