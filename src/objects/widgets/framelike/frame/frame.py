# FRAME
from typing import Tuple, List

from objects.datatypeConsts import str_t, name_t, int_t, bool_t, intList_t, floatList_t
from objects.interfaces import Container
from objects.parseObject import Widget

FRAME_VALID_PARAM: List[Tuple[str, str, str]] = [
    ('internalPadding', 'padding', intList_t),
    ('borderWidth', 'borderwidth', int_t),
    ('takeFocus', 'takefocus', bool_t),
    ('width', 'width', int_t),
    ('height', 'height', int_t)
]

GRID = [
    ('rowWeights', '', floatList_t),
    ('colWeights', '', floatList_t)
]

LABEL = [
    ('label', 'text', str_t),
    ('labelAnchor', 'labelanchor', str_t),
    ('labelWidget', 'labelwidget', name_t),
    ('labelAcceleratorIdx', 'underline', int_t)
]


class Frame(Widget, Container):
    def load(self, objName: str, *, placement=None):
        pass

    def postInit(self):
        pass

    def __init__(self, name: str):
        super().__init__(name, FRAME_VALID_PARAM + GRID + LABEL, [])

    def outputParams(self):
        pass

    def declaration(self):
        pass
