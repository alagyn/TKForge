from objects.datatypeConsts import color_t, int_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, focus_s, readonly_s

SPINBOX_STYLE = [
    ('arrowColor', color_t),
    ('arrowSize', int_t),
    ('background', color_t),  # Internal fieldbackground
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('textColor', color_t),
    ('lightColor', color_t),
    ('padding', intList_t),
    ('selectedBG', color_t),
    ('selectedTextColor', color_t)
]

SPINBOX_STATES = [
    active_s, disabled_s, focus_s, readonly_s
]


class SpinboxStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SPINBOX_STYLE, SPINBOX_STATES)
