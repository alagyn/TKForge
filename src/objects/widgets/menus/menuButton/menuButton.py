from objects.datatypeConsts import bool_t, str_t, name_t, int_t
from objects.interfaces import Container
from objects.parseObject import Widget

MENU_BUTTON_PARAM = [
    ('takeFocus', 'takefocus', bool_t),
    ('defaultText', 'text', str_t),
    ('textVariable', 'textvariable', name_t),
    ('acceleratorIdx', 'underline', int_t),
    ('width', 'width', int_t),
    ('direction', 'direction', str_t)
]

MENULIST = [
    ('menuList', '', name_t)
]

MENU_BUTTON_REC = [
    'menuList'
]


class MenuButton(Widget, Container):
    def load(self, objName: str, *, placement=None):
        pass

    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, MENU_BUTTON_PARAM + MENULIST, MENU_BUTTON_REC)
