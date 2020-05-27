# MenuList
from objects.interfaces import Container
from objects.parseObject import Widget


class MenuList(Widget, Container):

    def load(self, objName: str, *, placement=None):
        pass

    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, [], [])
