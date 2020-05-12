from typing import List, Set, Dict
from build.objects.parseObject import ParseObject, Style
from exceptions.forgeException import ReDefinitionException, ClaimException, ReStyleException


class BuildObject:
    def __init__(self):
        self.imports: List[str] = []
        self.defined: Dict[str, ParseObject] = {}
        self.undefined: Set[str] = set()
        self.claimed: Dict[str, str] = {}

        self.styles: Dict[str, Style] = {}

    def defineObject(self, name: str, obj: ParseObject):
        if name in self.defined:
            raise ReDefinitionException(name)

        self.defined[name] = obj

    def claimObject(self, childName: str, parentName: str):
        if childName in self.claimed:
            raise ClaimException(childName, self.claimed[childName], parentName)

        self.claimed[childName] = parentName
        if childName not in self.defined:
            self.undefined.add(childName)

    def addStyle(self, name: str, s: Style):
        if name in self.styles:
            raise ReStyleException(name)

        self.styles[name] = s