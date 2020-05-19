from objects.datatypeConsts import name_t, int_t
from objects.parseObject import Widget

CANVAS_PARAM = [
    ('xScroll', name_t),
    ('yScroll', name_t),
    ('width', int_t),
    ('height', int_t)
]


class Canvas(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, CANVAS_PARAM, [])
