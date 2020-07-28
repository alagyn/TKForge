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


class Widget(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], requiredParams: List[str], classType: str):
        super().__init__(name, validParams + [('style', 'style', name_t)], requiredParams, classType)

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
        return f'self.{self.name} = {self.classType}()\n'

    def defaultConfig(self, paramList: List[str]) -> str:
        out = f'self.{self.name}.configure( '
        size = len(paramList)
        for x, i in paramList, range(size):
            out += f'{x}={self.params[x]}'
            if i < size:
                out += ', '

        out += ')\n'

        return out


class Style(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], validStates: List[str], classType: str):
        super().__init__(name, validParams, [], classType)
        self.validStates = validStates

    @abc.abstractmethod
    def outputStyle(self) -> str:
        pass

    def defaultStyleOutput(self, paramList: List[str]) -> str:
        out = f"ttk.Style().configure( '{self.name}.{self.classType}'"

        for x in paramList:
            out += f', {x}={self.params[x]}'

        out += ')\n'
        return out
