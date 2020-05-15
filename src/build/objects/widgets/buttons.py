from ..parseObject import Style, Widget
from ...buildConsts import intList_t, str_t, int_t, bool_t, func_t, name_t, color_t
from ...buildConsts import active_s, disabled_s, pressed_s, readonly_s, alternate_s, selected_s
from exceptions.forgeException import DevException

BUTTON_BASE_V = [
    ('imageLoc', str_t),  # Internal "compound"
    ('image', str_t),
    ('takeFocus', bool_t),
    ('defaultText', str_t),
    ('textVariable', name_t),
    ('underline', int_t),  # TODO button accelerator
    ('width', int_t),
    ('command', func_t)
]

BUTTON_STYLE_BASE = [
    ('background', color_t),
    ('textColor', color_t),
    ('padding', intList_t)
]


class Button(Widget):
    def __init__(self, name):
        BUTTON_V = [
            ('defaultState', str_t)
        ]

        BUTTON_REC = ['command']

        super().__init__(name, BUTTON_BASE_V + BUTTON_V, BUTTON_REC)


class ButtonStyle(Style):
    def __init__(self, name):
        valid_param = [
            ('anchor', str_t),
            ('borderColor', color_t),
            ('darkColor', color_t),
            ('font', str_t),
            ('highlightColor', color_t),
            ('hightlightThickness', int_t),
            ('lightColor', color_t),
            ('relief', str_t),
            ('buttonDepth', int_t),  # Internal shiftrelief
            ('width', int_t)
        ]

        valid_states = [
            active_s, disabled_s, pressed_s, readonly_s
        ]
        super().__init__(name, valid_param + BUTTON_STYLE_BASE, valid_states)


class CheckButton(Widget):
    def __init__(self, name):
        CHECK_V = [
            ('onValue', str_t),
            ('offValue', str_t),
            ('outputVariable', name_t)
        ]

        CHECK_REC = [
            'onValue', 'offValue', 'outputVariable'
        ]

        super().__init__(name, BUTTON_BASE_V + CHECK_V, CHECK_REC)


class RadioButton(Widget):
    def __init__(self, name):
        RADIO_V = [
            ('onValue', str_t),
            ('outputVariable', name_t)
        ]

        RADIO_REC = [
            'onValue', 'outputVariable'
        ]
        super().__init__(name, BUTTON_BASE_V + RADIO_V, RADIO_REC)


# Used for Check/Radio Button
class SelectionStyle(Style):
    def __init__(self, name, buttonType: str):
        SELECTION_STYLE_BASE = [
            ('indicatorBackground', color_t),
            ('indicatorColor', color_t),
            ('indicatorPadding', intList_t),
            ('indicatorRelief', str_t)
        ]

        selection_states = [
            active_s, alternate_s, disabled_s, pressed_s, readonly_s, selected_s
        ]

        super().__init__(name, SELECTION_STYLE_BASE + BUTTON_STYLE_BASE, selection_states)

        RADIO = 1
        CHECK = 2

        if buttonType == 'radio':
            self.type = RADIO
        elif buttonType == 'check':
            self.type = CHECK
        else:
            raise DevException(f'Invalid Selection button type "{buttonType}"')



# TODO ListButton aka menubutton
