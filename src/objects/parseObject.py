import abc
from typing import Dict, Any, Set, Tuple

from forgeExceptions import *
from objects.datatypeConsts import name_t


class ParseObject(abc.ABC):
    """
    TopLevel abstract for a parsed object
    """

    def __init__(self, name: str, validParams: List[Tuple[str, str, str]], recommParams: List[str]):
        """
        Constructor

        :param name: The object's name
        :param validParams: List of tuples containing the parameter name and datatype string
        :param recommParams: List of reccomended parameters, must be subset of validParams
        """
        super().__init__()
        self.name: str = name

        # Generate Dictionary of parameter names and datatypes
        self.validParameters: Dict[str, str] = {k: v for k, v in validParams}
        self.recommendedParameters: Set[str] = set(recommParams)

        # Dev check for required params
        for x in recommParams:
            if x not in self.validParameters:
                raise DevException(f'Object {self.name}, required param "{x}" not in valid param list')

        # Container for parameter values given by the user
        self.definedParams: Set[str] = set()

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

    def checkReccommendedParams(self) -> None:
        """
        Final check to see if all recommended parameters have been set
        """
        for param in self.recommendedParameters:
            if param not in self.definedParams:
                print(f'Object {self.name}: recommend defining parameter "{param}"')


class Widget(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], requiredParams: List[str]):
        super().__init__(name, validParams + [('style', 'style', name_t)], requiredParams)
        self.params: Dict[str, Any] = {}

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

    def setWidgetParam(self, key: str, value: Any) -> None:
        """
        Sets the value of a parameter

        :param key: The parameter name
        :param value: The parameter's value
        """
        if key not in self.validParameters:
            raise InvalidParamException(self.name, key)

        self.params[key] = value

    def defaultInit(self, classType) -> str:
        return f'self.{self.name} = {classType}()\n'

    def defaultConfig(self, paramList: List[str]) -> str:
        out = f'self.{self.name}.configure( '
        size = len(paramList)
        for x, i in paramList, range(size):
            if x in self.params:
                out += f'{x}={self.params[x]}'
                if i < size:
                    out += ', '

        out += ')\n'

        return out


class Style(ParseObject, abc.ABC):
    def __init__(self, name, validParams: List[Tuple[str, str, str]], validStates: List[str]):
        super().__init__(name, validParams, [])
        self.validStates = validStates
        self.params: Dict[str, List[List[Any]]] = {}

    @abc.abstractmethod
    def outputStyle(self) -> str:
        pass

    def setStyleParam(self, key: str, value: Any, states: List[str]) -> None:
        if key not in self.validParameters:
            raise InvalidParamException(self.name, key)

        for x in states:
            if x not in self.validStates:
                raise InvalidStyleStateException(self.name, key, x)

        if key not in self.params:
            self.params[key] = []

        states.append(value)

        self.params[key].append(states)
        self.definedParams.add(key)

    def defaultStyleOutput(self, paramList: List[str], classType) -> str:

        out = f"ttk.Style().map( '{self.name}.{classType}'"

        for x in paramList:
            if x in self.definedParams:
                states = self.params[x]
                out += f', {x}=['
                length = len(states)
                for item, i in states, range(length):
                    out += f'{item}'
                    if i < length:
                        out += ','

                out += f']'

        out += ')\n'
        return out
