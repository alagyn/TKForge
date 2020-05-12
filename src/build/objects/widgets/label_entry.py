from ..parseObject import Widget, Style
from ...buildConsts import str_t, int_t, bool_t, color_t, intList_t, name_t, func_t, disabled_s, readonly_s, focus_s

# Label
LABEL_VALID = [
    ('imageLoc', str_t),
    ('image', str_t),
    ('padding', intList_t),
    ('takeFocus', bool_t),
    ('text', str_t),
    ('inputVariable', name_t),
    ('width', int_t),
    ('justify', str_t),
    ('defaultState', str_t),
    ('anchor', str_t),
    ('wrapLength', int_t),
    ('underline', bool_t),
    ('relief', str_t)
]

LABEL_REC = [
    # Intentionally left blank
]


class Label(Widget):
    def __init__(self, name):
        super().__init__(name, LABEL_VALID, LABEL_REC)


LABEL_STYLE_PARAM = [
    ('background', color_t),
    ('textColor', color_t),
    ('font', str_t)
]

LABEL_STATES = [disabled_s, readonly_s]


class LabelStyle(Style):
    def __init__(self, name):
        super().__init__(name, LABEL_STYLE_PARAM, LABEL_STATES)


# Entry
ENTRY_VALID = [
    ('takeFocus', bool_t),
    ('justify', str_t),
    ('passwordChar', str_t),
    ('defaultState', str_t),
    ('outputVariable', name_t),
    ('width', int_t),
    ('validateMode', str_t),
    ('validateCommand', func_t),
    ('xScroll', name_t)
]

ENTRY_REC = [
    # Intentionally left blanl
]


class Entry(Widget):
    def __init__(self, name):
        super().__init__(name, ENTRY_VALID, ENTRY_REC)


ENTRY_STATES = [disabled_s, focus_s, readonly_s]

ENTRY_STYLE_PARAM = [
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('fieldBG', color_t),
    ('textColor', color_t),
    ('lightColor', color_t),
    ('padding', intList_t),
    ('relief', str_t),
    ('selectedBG', color_t),
    ('selectedTextColor', color_t),
    ('selectedBorderWidth', int_t)
]