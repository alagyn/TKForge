

# WINDOW
from typing import List, Tuple

from objects.datatypeConsts import intList_t, int_t, bool_t, floatList_t, str_t, func_t, name_t
from objects.interfaces import Container
from objects.parseObject import Widget

WINDOW_VALID_PARAM: List[Tuple[str, str]] = [
    ('internalPadding', intList_t),
    ('borderWidth', int_t),
    ('takeFocus', bool_t),
    ('rowWeights', floatList_t),
    ('colWeights', floatList_t),
    ('title', str_t),
    ('size', intList_t),
    ('initOperation', func_t),
    ('exitOperation', func_t),
    ('loc', intList_t),
    ('menubar', name_t)
]

WINDOW_REC_PARAM: List[str] = [
    'title', 'size', 'initOperation', 'exitOperation',
]


class Window(Widget, Container):
    # TODO Window output
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def load(self, obj):
        pass

    def __init__(self, name):
        super().__init__(name, WINDOW_VALID_PARAM, WINDOW_REC_PARAM)
