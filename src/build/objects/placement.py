from .parseObject import ParseObject
from typing import List, Tuple

from ..buildConsts import intList_t, floatList_t, int_t, strList_t

PLACE_VALID_PARAMS: List[Tuple[str, str]] = [
    ('gridLoc', intList_t),
    ('weight', floatList_t),
    ('rowspan', int_t),
    ('colspan', int_t),
    ('externPadding', intList_t),
    ('sticky', strList_t)
]

PLACE_REQ_PARAM: List[str] = [
    'gridLoc'
]


class Placement(ParseObject):
    def loadObject(self, obj, placement):
        pass

    def __init__(self, name: str):
        super().__init__(name, PLACE_VALID_PARAMS, PLACE_REQ_PARAM)
