from typing import List, Dict, Any, Set, Tuple
import abc

from forgeExceptions import *
from objects.datatypeConsts import TO_ENUM, name_t


class ParseObject(abc.ABC):
    """
    TopLevel abstract for a parsed object
    """

    def __init__(self, name: str, validParams: List[Tuple[str, str]], recommParams: List[str]):
        """
        Constructor

        :param name: The object's name
        :param validParams: List of tuples containing the parameter name and datatype string
        :param recommParams: List of reccomended parameters, must be subset of validParams
        """
        super().__init__()
        self.name: str = name

        # Generate Dictionary of parameter names and datatypes
        self.validTypes = [TO_ENUM[y] for x, y in validParams]
        self.validParameters: Dict[str, int] = {k: v for k, v in zip(validParams, self.validTypes)}
        self.recommendedParameters: Set[str] = set(recommParams)

        # Dev check for required params
        for x in recommParams:
            if x not in self.validParameters:
                raise DevException(f'Object {self.name}, required param "{x}" not in valid param list')

        # Container for parameter values given by the user
        self.params: Dict[str, Any] = {}

    def setParam(self, key: str, value: Any, datatype: int) -> None:
        """
        Sets the value of a parameter

        :param key: The parameter name
        :param value: The parameter's value
        :param datatype: The value's datatype enum
        """
        if key in self.validParameters:
            if datatype != self.validParameters[key]:
                raise InvalidTypeException(self.name, key, self.validParameters[key], datatype)

            self.params[key] = value

        else:
            raise InvalidParamException(self.name, key)

    def checkRequiredParams(self) -> None:
        """
        Final check to see if all recommended parameters have been set
        """
        for param in self.recommendedParameters:
            if param not in self.params:
                print(f'Object {self.name}: recommend defining parameter "{param}"')


class Widget(ParseObject):
    def __init__(self, name, validParams: List[Tuple[str, str]], requiredParams: List[str]):
        super().__init__(name, validParams + [('style', name_t)], requiredParams)


class Style(ParseObject):
    def __init__(self, name, validParams: List[Tuple[str, str]], validStates: List[str]):
        super().__init__(name, validParams, [])
        self.validStates = validStates
