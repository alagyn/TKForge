from .parseObject import ParseObject
from typing import List, Tuple

from ..buildConsts import intList_t, floatList, int_t, strList

PLACE_VALID_PARAMS: List[Tuple[str, str]] = [
    ('gridLoc', intList_t),
    ('weight', floatList),
    ('rowspan', int_t),
    ('colspan', int_t),
    ('externPadding', intList_t),
    ('sticky', strList)
]

PLACE_REQ_PARAM: List[str] = [
    'gridLoc'
]


class Placement(ParseObject):
    def loadObject(self, obj, placement):
        pass

    def __init__(self, name: str):
        super().__init__(name, PLACE_VALID_PARAMS, PLACE_REQ_PARAM)
