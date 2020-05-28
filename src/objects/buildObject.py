from typing import List, Set, Dict
from objects.parseObject import Style, ParseObject
from forgeExceptions import ReDefinitionException, ClaimException, ReStyleException, UndefinedException


class BuildObject:
    def __init__(self):
        """
        Initializes a new empty BuildObject
        """

        # List of python imports for functions
        self.imports: List[str] = []

        # Dict of every object that has been defined
        # K: name of object
        # V: The object
        self.defined: Dict[str, ParseObject] = {}

        # Set of object names that have been loaded but not defined
        self.undefined: Set[str] = set()

        # Set of Dict of object names that have been loaded
        # K: child name
        # V: parent name
        self.claimed: Dict[str, str] = {}

        # Dict of defined styles
        # K: Style name
        # V: Style object
        self.styles: Dict[str, Style] = {}

    def defineObject(self, obj: ParseObject):
        """
        Adds a new object to the defined list

        :raises: ReDefinitionException if the objects name already exists
        :param obj:
        """
        if obj.name in self.defined:
            raise ReDefinitionException(obj.name)

        if obj.name in self.undefined:
            self.undefined.remove(obj.name)

        self.defined[obj.name] = obj

    def claimObject(self, childName: str, parentName: str):
        """
        Claims an object that has been loaded

        :raises: ClaimException if the child has already been claimed
        :param childName: The child object's name
        :param parentName: The parent object's name
        """
        if childName in self.claimed:
            raise ClaimException(childName, self.claimed[childName], parentName)

        self.claimed[childName] = parentName
        if childName not in self.defined:
            self.undefined.add(childName)

    def addStyle(self, s: Style):
        """
        Adds a style to the list

        :raises: ReStyleException if the a style with the same name already exists
        :param s: The new style
        :return:
        """
        if s.name in self.styles:
            raise ReStyleException(s.name)

        self.styles[s.name] = s

    def checkClaims(self):
        """
        Checks if every name that has been claimed was defined.
        :return: None, raises parseException if failure
        """

        if len(self.undefined) > 0:
            UndefinedException(list(self.undefined))