from objects.datatypeConsts import color_t, str_t, intList_t, int_t
from objects.stateConsts import disabled_s, focus_s, pressed_s, readonly_s
from objects.parseObject import Style

STYLE_PARAM = [
    ('arrowColor', color_t),
    ('arrowSize', int_t),
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('focusFill', color_t),
    ('textColor', color_t),
    ('fieldBG', color_t),
    ('insertCaratWidth', int_t),
    ('lightColor', int_t),
    ('padding', intList_t),
    ('selectedBG', color_t),
    ('selectedTextColor', color_t),
    ('borderWidth', int_t),
    ('relief', str_t),

    # TODO test if combobox listbox styling works
    ('listBG', color_t),
    ('listFont', str_t),
    ('listTextColor', color_t),
    ('listSelectedBG', color_t),
    ('listSelectedTextColor', color_t)
]

STATES = [
    disabled_s, focus_s, pressed_s, readonly_s
]


class ComboboxStyle(Style):
    def __init__(self, name):
        super().__init__(name, STYLE_PARAM, STATES)
