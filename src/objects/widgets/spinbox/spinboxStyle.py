from objects.datatypeConsts import color_t, int_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, focus_s, readonly_s

SPINBOX_STYLE = [
    ('arrowColor', 'arrowcolor', color_t),
    ('arrowSize', 'arrowsize', int_t),
    ('background', 'fieldbackground', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('textColor', 'foreground', color_t),
    ('lightColor', 'lightcolor', color_t),
    ('padding', 'padding', intList_t),
    ('selectedBG', 'selectedbackground', color_t),
    ('selectedTextColor', 'selectedforeground', color_t)
]

SPINBOX_STATES = [
    active_s, disabled_s, focus_s, readonly_s
]


class SpinboxStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SPINBOX_STYLE, SPINBOX_STATES)
