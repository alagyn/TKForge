from objects.interfaces import Container
from objects.parseObject import Widget
from objects.datatypeConsts import color_t, int_t, bool_t, str_t

MENU_PARAM = [
    ('activeBG', 'activebackground', color_t),
    ('activeBorderWidth', 'activeborderwidth', int_t),
    ('activeTextColor', 'activeforeground', color_t),
    ('background', 'background', color_t),
    ('borderWidth', 'borderwidth', int_t),
    ('disabledTextColor', 'sisabledforeground', color_t),
    ('font', 'font', str_t),
    ('textColor', 'foreground', color_t),
    ('relief', 'relief', str_t),
    ('takeFocus', 'takefocus', bool_t),
    ('selectColor', 'selectcolor', color_t)
]


class MenuBar(Widget, Container):

    def load(self, objName: str, *, placement=None):
        pass

    def __init__(self, name):
        super().__init__(name, MENU_PARAM, [])

    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass
