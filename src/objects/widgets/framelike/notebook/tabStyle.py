from objects.datatypeConsts import color_t, intList_t, str_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, selected_s

TAB_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('expand', intList_t),
    ('font', str_t),
    ('textColor', color_t),
    ('padding', intList_t)
]

TAB_STATES = [
    active_s, disabled_s, selected_s
]


class NotebookTabStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, TAB_STYLE, TAB_STATES)

