from objects.datatypeConsts import str_t, strList_t, bool_t, float_t, int_t
from .parseObject import ParseObject


class Variable(ParseObject):
    def __init__(self, name, datatype):
        super().__init__(name, [('value', 'value', datatype)], ['value'])


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
