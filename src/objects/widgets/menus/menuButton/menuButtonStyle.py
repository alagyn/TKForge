from objects.datatypeConsts import int_t, color_t, str_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import active_s, disabled_s, readonly_s

MENU_BUTTON_STYLE = [
    ('arrowSize', 'arrowsize', int_t),
    ('background', 'background', color_t),
    ('imageLoc', 'compound', str_t),
    ('textColor', 'foreground', color_t),
    ('font', 'font', str_t),
    ('padding', 'padding', intList_t),
    ('relief', 'relief', str_t)
]

IMAGE = [
    ('image', str_t)
]

MENU_BUTTON_STATES = [
    active_s, disabled_s, readonly_s
]


class MenuButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, MENU_BUTTON_STYLE, MENU_BUTTON_STATES)
