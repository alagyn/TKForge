from abc import ABC

from objects.parseObject import Style
from objects.stateConsts import active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
from objects.datatypeConsts import *
from forgeExceptions import DevException

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


# Used for Check/Radio Button
class SelectionStyle(Style, ABC):
    def __init__(self, name, buttonType: str):

        super().__init__(name, SELECTION_STYLE_BASE + IMAGE, selection_states)

        RADIO = 1
        CHECK = 2

        if buttonType == 'radio':
            self.type = RADIO
        elif buttonType == 'check':
            self.type = CHECK
        else:
            raise DevException(f'Invalid Selection button type "{buttonType}"')


class RadioButtonStyle(SelectionStyle):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, 'radio')


class CheckButtonStyle(SelectionStyle):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, 'check')
