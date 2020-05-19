from objects.datatypeConsts import str_t, color_t, intList_t, int_t
from objects.stateConsts import active_s, disabled_s, pressed_s, readonly_s
from objects.parseObject import Style

BUTTON_STYLE = [
    ('background', color_t),
    ('textColor', color_t),
    ('padding', intList_t),
    ('anchor', str_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('font', str_t),
    ('highlightColor', color_t),
    ('hightlightThickness', int_t),
    ('lightColor', color_t),
    ('relief', str_t),
    ('buttonDepth', int_t),  # Internal shiftrelief
    ('width', int_t)
]

BUTTON_STATES = [
    active_s, disabled_s, pressed_s, readonly_s
]


class ButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, BUTTON_STYLE, BUTTON_STATES)
