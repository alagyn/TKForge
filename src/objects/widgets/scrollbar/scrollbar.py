from objects.datatypeConsts import bool_t, str_t
from objects.parseObject import Widget

SCROLL_VALID = [
    ('orient', 'orient', str_t),
    ('takeFocus', 'takefocus', bool_t)
]

SCROLL_REC = [
    'orient'
]


class Scrollbar(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


def __init__(self, name):
    super().__init__(name, SCROLL_VALID, SCROLL_REC)
