from objects.datatypeConsts import color_t, str_t, intList_t, int_t
from objects.stateConsts import disabled_s, focus_s, readonly_s
from objects.parseObject import Style

ENTRY_STATES = [disabled_s, focus_s, readonly_s]

ENTRY_STYLE_PARAM = [
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('fieldBG', 'fieldbackground', color_t),
    ('textColor', 'foreground', color_t),
    ('lightColor', 'lightcolor', color_t),
    ('padding', 'padding', intList_t),
    ('relief', 'relief', str_t),
    ('selectedBG', 'selectedbackground', color_t),
    ('selectedTextColor', 'selectedforeground', color_t),
    ('selectedBorderWidth', 'selectedborderwidth', int_t)
]


class EntryStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, ENTRY_STYLE_PARAM, ENTRY_STATES, 'TEntry')
