# NOTEBOOK
from typing import List, Tuple

from objects.datatypeConsts import bool_t, intList_t, int_t, floatList_t
from objects.interfaces import Container
from objects.parseObject import Widget

NOTEBOOK_VALID_PARAM: List[Tuple[str, str, str]] = [
    ('internalPadding', 'padding', intList_t),
    ('takeFocus', 'takefocus', bool_t),
    ('width', 'width', int_t),
    ('height', 'height', int_t)
]

NOTEBOOK_REC_PARAM: List[str] = []


class Notebook(Widget, Container):
    def load(self, objName: str, *, placement=None):
        pass

    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, NOTEBOOK_VALID_PARAM, NOTEBOOK_REC_PARAM)
