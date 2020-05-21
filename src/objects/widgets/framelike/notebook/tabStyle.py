from objects.datatypeConsts import color_t, intList_t, str_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, selected_s

TAB_STYLE = [
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('expand', 'expand', intList_t),
    ('font', 'font', str_t),
    ('textColor', 'foreground', color_t),
    ('padding', 'padding', intList_t)
]

IMAGE = [
    ('imageLoc', 'compound', str_t)
]

TAB_STATES = [
    active_s, disabled_s, selected_s
]


class NotebookTabStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, TAB_STYLE + IMAGE, TAB_STATES)

