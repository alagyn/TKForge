from objects.datatypeConsts import color_t, int_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s

SCROLL_STYLE_STATES = [active_s, disabled_s]

SCROLL_STYLE_PARAM = [
    ('arrowColor', 'arrowcolor', color_t),
    ('arrowSize', 'arrowsize', int_t),
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('foreground', 'foreground', color_t),
    ('gripCount', 'gripcount', int_t),
    ('lightColor', 'lightcolor', int_t),
    ('troughColor', 'troughcolor', color_t)
]


class ScrollbarStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SCROLL_STYLE_PARAM, SCROLL_STYLE_STATES)
