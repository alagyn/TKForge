from objects.datatypeConsts import color_t
from objects.parseObject import Style

PROGRESS_STYLE_PARAM = [
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('lightColor', 'lightcolor', color_t),
    ('troughColor', 'troughcolor', color_t)
]


class ProgressbarStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, PROGRESS_STYLE_PARAM, [])
