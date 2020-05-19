from objects.datatypeConsts import color_t
from objects.parseObject import Style

PROGRESS_STYLE_PARAM = [
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('lightColor', color_t),
    ('troughColor', color_t)
]


class ProgressbarStyle(Style):
    def __init__(self, name):
        super().__init__(name, PROGRESS_STYLE_PARAM, [])
