# MenuList
from objects.interfaces import Container
from objects.parseObject import Widget


class MenuList(Widget, Container):

    def load(self, objName: str, *, placement=None):
        pass

    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, [], [])
