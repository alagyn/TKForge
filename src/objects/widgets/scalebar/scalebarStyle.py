from objects.datatypeConsts import color_t, int_t, str_t
from objects.parseObject import Style
from objects.stateConsts import active_s

SCALE_STYLE_STATES = [active_s]

SCALE_STYLE_PARAM = [
    ('background', 'background', color_t),
    ('borderWidth', 'borderwidth', int_t),
    ('darkColor', 'darkcolor', color_t),
    ('grooveWidth', 'groovewidth', int_t),
    ('lightColor', 'lightcolor', color_t),
    ('sliderWidth', 'sliderwidth', int_t),
    ('troughColor', 'troughcolor', color_t),
    ('troughRelief', 'troughrelief', str_t)
]


class ScalebarStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SCALE_STYLE_PARAM, SCALE_STYLE_STATES)
