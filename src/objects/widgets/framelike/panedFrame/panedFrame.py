from objects.datatypeConsts import int_t, bool_t, str_t
from objects.interfaces import Container
from objects.parseObject import Widget

PANED_FRAME_PARAM = [
    ('takeFocus', 'takefocus', bool_t),
    ('orient', 'orient', str_t),
    ('width', 'width', int_t),
    ('height', 'height', int_t)
]

PANED_FRAME_REC = [
    'orient'
]


class PanedFrame(Widget, Container):
    def load(self, objName: str, *, placement=None):
        pass

    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, PANED_FRAME_PARAM, PANED_FRAME_REC)
