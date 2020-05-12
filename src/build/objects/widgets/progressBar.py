from ..parseObject import Widget, Style

from ...buildConsts import str_t, int_t, name_t, float_t, bool_t, color_t

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


class ProgressBar(Widget):
    def __init__(self, name):
        super().__init__(name, PROGRESS_BAR_VALID, PROGRESS_BAR_REC)


PROGRESS_STYLE_PARAM = [
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('lightColor', color_t),
    ('troughColor', color_t)
]


class ProgressBarStyle(Style):
    def __init__(self, name):
        super().__init__(name, PROGRESS_STYLE_PARAM, [])
