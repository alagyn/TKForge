from objects.interfaces import Container
from objects.parseObject import Widget
from objects.datatypeConsts import color_t, int_t, bool_t, str_t

MENU_PARAM = [
    ('activeBG', color_t),
    ('activeBorderWidth', int_t),
    ('activeTextColor', color_t),
    ('background', color_t),
    ('borderWidth', int_t),
    ('disabledTextColor', color_t),
    ('font', str_t),
    ('textColor', color_t),
    ('relief', str_t),
    ('takeFocus', bool_t),
    ('selectColor', color_t)
]


class MenuBar(Widget, Container):
    def load(self, obj):
        pass

    def __init__(self, name):
        super().__init__(name, MENU_PARAM, [])

    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass
