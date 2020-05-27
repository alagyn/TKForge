# WINDOW
from typing import List, Tuple

from objects.datatypeConsts import intList_t, int_t, bool_t, floatList_t, str_t, name_t
from objects.interfaces import Container
from objects.parseObject import Widget

WINDOW_VALID_PARAM: List[Tuple[str, str, str]] = [
    ('internalPadding', 'padding', intList_t),
    ('borderWidth', 'borderwidth', int_t),
    ('takeFocus', 'takefocus', bool_t),
    ('width', 'width', int_t),
    ('height', 'height', int_t)
]

DATA_PARAM = [
    ('title', '', str_t),
    ('loc', '', intList_t),
    ('menubar', '', name_t)
]

GRID_PARAM = [
    ('rowWeights', '', floatList_t),
    ('colWeights', '', floatList_t)
]

WINDOW_REC_PARAM: List[str] = [
    'title', 'size', 'initOperation', 'exitOperation',
]


class Window(Widget, Container):
    def load(self, objName: str, *, placement=None):
        pass

    def declaration(self):
        # Gen init and exit functions for clients

        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, WINDOW_VALID_PARAM + DATA_PARAM + GRID_PARAM, WINDOW_REC_PARAM)
