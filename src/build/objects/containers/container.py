from build.objects.parseObject import Widget, ParseObject
from build.objects.placement import Placement
from typing import List, Tuple, Dict


class Container(Widget):
    def __init__(self, name: str, validParams: List[Tuple[str, str]], requiredParams: List[str]):
        super().__init__(name, validParams, requiredParams)

        self.objects: Dict[Widget, Placement] = {}

    def loadObj(self, obj: Widget, placement: Placement):
        if obj not in self.objects:
            self.objects[obj] = placement
