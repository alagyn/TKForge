from objects.parseObject import Style
from objects.stateConsts import active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
from objects.datatypeConsts import *
from forgeExceptions import DevException

# TOFIX Check selection style params

SELECTION_STYLE_BASE = [
    ('indicatorBackground', color_t),
    ('indicatorColor', color_t),
    ('indicatorPadding', intList_t),
    ('indicatorRelief', str_t)
]

selection_states = [
    active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
]


# Used for Check/Radio Button
class SelectionStyle(Style):
    def __init__(self, name, buttonType: str):

        super().__init__(name, SELECTION_STYLE_BASE, selection_states)

        RADIO = 1
        CHECK = 2

        if buttonType == 'radio':
            self.type = RADIO
        elif buttonType == 'check':
            self.type = CHECK
        else:
            raise DevException(f'Invalid Selection button type "{buttonType}"')
