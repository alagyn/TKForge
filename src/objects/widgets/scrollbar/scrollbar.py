from objects.datatypeConsts import bool_t, str_t
from objects.parseObject import Widget

SCROLL_VALID = [
    ('orient', str_t),
    ('takeFocus', bool_t)
]

SCROLL_REC = [
    'orient'
]


class Scrollbar(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, SCROLL_VALID, SCROLL_REC)
