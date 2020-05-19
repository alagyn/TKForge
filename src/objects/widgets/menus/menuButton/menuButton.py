from objects.datatypeConsts import bool_t, str_t, name_t, int_t
from objects.interfaces import Container
from objects.parseObject import Widget

MENU_BUTTON_PARAM = [
    ('takeFocus', bool_t),
    ('defaultText', str_t),
    ('textVariable', name_t),
    ('accelerator', int_t),  # TODO menuButton accelerator
    ('width', int_t),
    ('direction', str_t),
    ('menuList', name_t)
]

MENU_BUTTON_REC = [
    'menuList'
]


class MenuButton(Widget, Container):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def load(self, obj):
        pass

    def __init__(self, name):
        super().__init__(name, MENU_BUTTON_PARAM, MENU_BUTTON_REC)
