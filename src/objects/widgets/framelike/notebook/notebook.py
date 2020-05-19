# NOTEBOOK
from typing import List, Tuple

from objects.datatypeConsts import nameList_t, bool_t, intList_t, int_t, floatList_t
from objects.interfaces import Container
from objects.parseObject import Widget

NOTEBOOK_VALID_PARAM: List[Tuple[str, str]] = [
    ('internalPadding', intList_t),
    ('borderWidth', int_t),
    ('takeFocus', bool_t),
    ('rowWeights', floatList_t),
    ('colWeights', floatList_t),
    ('tabs', nameList_t),
    ('takeFocus', bool_t)
]

NOTEBOOK_REC_PARAM: List[str] = ['tabs']


class Notebook(Widget, Container):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def load(self, obj):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, NOTEBOOK_VALID_PARAM, NOTEBOOK_REC_PARAM)
