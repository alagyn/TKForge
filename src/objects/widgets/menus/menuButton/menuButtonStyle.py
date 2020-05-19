from objects.datatypeConsts import int_t, color_t, str_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, readonly_s

MENU_BUTTON_STYLE = [
    ('arrowSize', int_t),
    ('background', color_t),
    ('imageLoc', str_t),
    ('image', str_t),
    ('textColor', color_t),
    ('font', str_t),
    ('padding', intList_t),
    ('relief', str_t)
]

MENU_BUTTON_STATES = [
    active_s, disabled_s, readonly_s
]


class MenuButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, MENU_BUTTON_STYLE, MENU_BUTTON_STATES)
