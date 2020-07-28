from objects.datatypeConsts import name_t, int_t
from objects.parseObject import Widget

CANVAS_PARAM = [
    ('width', 'width', int_t),
    ('height', 'height', int_t)
]

SCROLL = [
    ('xScroll', '', name_t),
    ('yScroll', '', name_t)
]


class Canvas(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, CANVAS_PARAM + SCROLL, [])
