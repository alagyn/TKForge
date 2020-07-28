from objects.datatypeConsts import str_t, color_t, intList_t, int_t
from objects.stateConsts import active_s, disabled_s, pressed_s, readonly_s
from objects.parseObject import Style

BUTTON_STYLE = [
    ('background', 'background', color_t),
    ('textColor', 'foreground', color_t),
    ('padding', 'padding', intList_t),
    ('anchor', 'anchor', str_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('font', 'font', str_t),
    ('highlightColor', 'highlightcolor', color_t),
    ('hightlightThickness', 'highlightthickness', int_t),
    ('lightColor', 'lightcolor', color_t),
    ('relief', 'relief', str_t),
    ('buttonDepth', 'shiftrelief', int_t),
    ('width', 'width', int_t),
    ('imageLoc', 'compound', str_t)
]

IMAGE_PARAM = [
    ('image', 'image', str_t)
]

BUTTON_STATES = [
    active_s, disabled_s, pressed_s, readonly_s
]


class ButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, BUTTON_STYLE + IMAGE_PARAM, BUTTON_STATES)
