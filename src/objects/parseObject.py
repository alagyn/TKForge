import abc
from typing import Dict, Any, Set, Tuple

from forgeExceptions import *
from objects.datatypeConsts import name_t


class ParseObject(abc.ABC):
    """
    TopLevel abstract for a parsed object
    """

    def __init__(self, name: str, validParams: List[Tuple[str, str, str]], recommParams: List[str], classType: str):
        """
        Constructor

        :param name: The object's name
        :param validParams: List of tuples containing the parameter name and datatype string
        :param recommParams: List of reccomended parameters, must be subset of validParams
        """
        super().__init__()
        self.name: str = name
        self.classType = classType

        # Generate Dictionary of parameter names and datatypes
        self.validParameters: Dict[str, str] = {k: v for k, v in validParams}
        self.recommendedParameters: Set[str] = set(recommParams)

        # Dev check for required params
        for x in recommParams:
            if x not in self.validParameters:
                raise DevException(f'Object {self.name}, required param "{x}" not in valid param list')

        # Container for parameter values given by the user
        self.params: Dict[str, Any] = {}

    def getDatatype(self, key: str) -> str:
        """
        Returs the datatype of the given parameter
        :param key: The parameter name/key
        :return: The datatype
        """

        try:
            return self.validParameters[key]
        except KeyError:
            raise InvalidParamException(self.name, key)

    def setParam(self, key: str, value: Any) -> None:
        """
        Sets the value of a parameter

        :param key: The parameter name
        :param value: The parameter's value
        """
        try:
            self.params[key] = value
        except KeyError:
            raise InvalidParamException(self.name, key)

    def checkReccommendedParams(self) -> None:
        """
        Final check to see if all recommended parameters have been set
        """
        for param in self.recommendedParameters:
            if param not in self.params:
                print(f'Object {self.name}: recommend defining parameter "{param}"')

    @abc.abstractmethod
    def outputInit(self):
        pass

    @abc.abstractmethod
    def outputConfig(self):
        pass

    @abc.abstractmethod
    def outputPost(self):
        pass

    @abc.abstractmethod
    def outputCommand(self):
        pass

    def defaultInit(self) -> str:
        return f'self.{self.name} = {self.classType}()'


class Widget(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], requiredParams: List[str]):
        super().__init__(name, validParams + [('style', 'style', name_t)], requiredParams)

    @staticmethod
    def printWidgetConfig(name: str, vals: List[Tuple[str, str]]) -> str:
        out = f'{name}.configure( '
        for x in range(0, len(vals)):
            out += f'{vals[x][0]}={vals[x][1]}'
            if x != len(vals):
                out += ', '

        out += ')\n'
        return out


class Style(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], validStates: List[str]):
        super().__init__(name, validParams, [])
        self.validStates = validStates

    @staticmethod
    def printStyleConfig(name: str, vals: List[Tuple[str, str]]) -> str:
        out = f'ttk.Style().configure("{name}"'
        for x in vals:
            out += f', {x[0]}={x[1]}'

        out += ')\n'
        return out

    @abc.abstractmethod
    def outputStyle(self):
        pass
