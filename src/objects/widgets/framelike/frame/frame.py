# FRAME
from typing import Tuple, List

from objects.datatypeConsts import str_t, name_t, int_t, bool_t, intList_t, floatList_t
from objects.interfaces import Container
from objects.parseObject import Widget

FRAME_VALID_PARAM: List[Tuple[str, str]] = [
    ('internalPadding', intList_t),
    ('borderWidth', int_t),
    ('takeFocus', bool_t),
    ('rowWeights', floatList_t),
    ('colWeights', floatList_t),
    ('label', str_t),
    ('labelAnchor', str_t),
    ('labelWidget', name_t),
    ('underline', int_t),  # TODO Labelframe accelerator
    ('takeFocus', bool_t)
]


class Frame(Widget, Container):
    def __init__(self, name: str):
        super().__init__(name, FRAME_VALID_PARAM, [])

    def outputParams(self):
        pass


    def load(self, obj):
        pass

    def declaration(self):
        pass
