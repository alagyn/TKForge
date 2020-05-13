from ..parseObject import Widget, Style

from ...buildConsts import str_t, strList_t, color_t, int_t, bool_t, name_t, intList_t
from ...buildConsts import disabled_s, focus_s, pressed_s, readonly_s

COMBO_BOX_VALID = [
    ('takeFocus', bool_t),
    ('justify', str_t),
    ('defaultState', str_t),
    ('outputVariable', name_t),
    ('values', strList_t),
    ('width', int_t),
    ('height', int_t)

]

COMBO_BOX_REC = [
    'values', 'outputVariable'
]


class ComboBox(Widget):
    def __init__(self, name):
        super().__init__(name, COMBO_BOX_VALID, COMBO_BOX_REC)


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


class ComboBoxStyle(Style):
    def __init__(self, name):
        super().__init__(name, STYLE_PARAM, STATES)
