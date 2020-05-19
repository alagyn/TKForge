from objects.datatypeConsts import intList_t, int_t, bool_t, floatList_t, str_t, nameList_t
from objects.interfaces import Container
from objects.parseObject import Widget

PANED_FRAME_PARAM = [
    ('internalPadding', intList_t),
    ('borderWidth', int_t),
    ('takeFocus', bool_t),
    ('rowWeights', floatList_t),
    ('colWeights', floatList_t),
    ('takeFocus', bool_t),
    ('orient', str_t),
    ('panes', nameList_t)
]

PANED_FRAME_REC = [
    'orient', 'panes'
]


class PanedFrame(Widget, Container):
    # TODO PanedFrame output
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def load(self, obj):
        pass

    def __init__(self, name):
        super().__init__(name, PANED_FRAME_PARAM, PANED_FRAME_REC)
