from .parseObject import ParseObject

from ..buildConsts import float_t, int_t, str_t, bool_t, strList_t


class Variable(ParseObject):
    def __init__(self, name, datatype):
        super().__init__(name, [('value', datatype)], ['value'])


class StringVariable(Variable):
    def __init__(self, name):
        super().__init__(name, str_t)


class IntVariable(Variable):
    def __init__(self, name):
        super().__init__(name, int_t)


class FloatVariable(Variable):
    def __init__(self, name):
        super().__init__(name, float_t)


class BoolVariable(Variable):
    def __init__(self, name):
        super().__init__(name, bool_t)


class ListVariable(Variable):
    def __init__(self, name):
        super().__init__(name, strList_t)
