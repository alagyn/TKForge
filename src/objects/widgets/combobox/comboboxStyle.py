from objects.datatypeConsts import color_t, str_t, intList_t, int_t
from objects.stateConsts import disabled_s, focus_s, pressed_s, readonly_s
from objects.parseObject import Style

STYLE_PARAM = [
    ('arrowColor', 'arrowcolor', color_t),
    ('arrowSize', 'arrowsize', int_t),
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('focusFill', 'focusfill', color_t),
    ('textColor', 'foreground', color_t),
    ('fieldBG', 'fieldbackground', color_t),
    ('insertCaratWidth', 'insertwidth', int_t),
    ('lightColor', 'lightcolor', int_t),
    ('padding', 'padding', intList_t),
    ('selectedBG', 'selectedbackground', color_t),
    ('selectedTextColor', 'selectedforeground', color_t)
]

POPDOWN = [
    ('popdownBorderWidth', 'borderwidth', int_t),
    ('popdownRelief', 'relief', str_t)
]

LIST = [
    # TODO test if combobox listbox styling works
    ('listBG', '', color_t),
    ('listFont', '', str_t),
    ('listTextColor', '', color_t),
    ('listSelectedBG', '', color_t),
    ('listSelectedTextColor', '', color_t)
]

STATES = [
    disabled_s, focus_s, pressed_s, readonly_s
]


class ComboboxStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, STYLE_PARAM + POPDOWN + LIST, STATES, 'TCombobox')
