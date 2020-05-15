from objects.datatypeConsts import color_t, int_t, str_t
from objects.parseObject import Style
from objects.stateConsts import active_s

SCALE_STYLE_STATES = [active_s]

SCALE_STYLE_PARAM = [
    ('background', color_t),
    ('borderWidth', int_t),
    ('darkColor', color_t),
    ('grooveWidth', int_t),
    ('lightColor', color_t),
    ('sliderWidth', int_t),
    ('troughColor', color_t),
    ('troughRelief', str_t)
]


class ScalebarStyle(Style):
    def __init__(self, name):
        super().__init__(name, SCALE_STYLE_PARAM, SCALE_STYLE_STATES)
