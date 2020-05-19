from objects.datatypeConsts import float_t, name_t
from objects.parseObject import Widget

PANE_PARAM = [
    ('weight', float_t),
    ('widget', name_t)
]

PANE_REC = ['widget']


class Pane(Widget):
    # TODO Pane output
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, PANE_PARAM, PANE_REC)
