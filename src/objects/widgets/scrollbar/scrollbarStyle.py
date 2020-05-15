from objects.datatypeConsts import color_t, int_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s

SCROLL_STYLE_STATES = [active_s, disabled_s]

SCROLL_STYLE_PARAM = [
    ('arrowColor', color_t),
    ('arrowSize', int_t),
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('foreground', color_t),
    ('gripCount', int_t),
    ('lightColor', int_t),
    ('troughColor', color_t)
]


class ScrollbarStyle(Style):
    def __init__(self, name):
        super().__init__(name, SCROLL_STYLE_PARAM, SCROLL_STYLE_STATES)
