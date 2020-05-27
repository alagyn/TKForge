from objects.datatypeConsts import float_t
from objects.parseObject import Widget

PANE_PARAM = [
    ('weight', 'weight', float_t)
]

PANE_REC = []


class Pane(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, PANE_PARAM, PANE_REC)
