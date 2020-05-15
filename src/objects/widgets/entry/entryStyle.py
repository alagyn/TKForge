from objects.datatypeConsts import color_t, str_t, intList_t, int_t
from objects.stateConsts import disabled_s, focus_s, readonly_s
from objects.parseObject import Style

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


class EntryStyle(Style):
    def __init__(self, name):
        super().__init__(name, ENTRY_STYLE_PARAM, ENTRY_STATES)
