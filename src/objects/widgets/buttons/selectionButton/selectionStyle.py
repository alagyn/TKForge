from objects.parseObject import Style
from objects.stateConsts import active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
from objects.datatypeConsts import *

SELECTION_STYLE_BASE = [
    ('background', 'background', color_t),
    ('textColor', 'foreground', color_t),
    ('imageLoc', 'compound', str_t),
    ('indicatorBG', 'indicatorbackground', color_t),
    ('indicatorColor', 'indicatorcolor', color_t),
    ('indicatorPadding', 'indicatormargin', intList_t),
    ('indicatorRelief', 'indicatorrelief', str_t),
    ('padding', 'padding', intList_t)
]

IMAGE = [
    ('image', '', str_t),
]

selection_states = [
    active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
]


class RadioButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SELECTION_STYLE_BASE + IMAGE, selection_states)


class CheckButtonStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, SELECTION_STYLE_BASE + IMAGE, selection_states)
