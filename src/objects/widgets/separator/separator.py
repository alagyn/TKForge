from objects.datatypeConsts import str_t, bool_t
from objects.parseObject import Widget

SEP_VALID = [
    ('takeFocus', 'takefocus', bool_t),
    ('orient', 'orient', str_t)
]

SEP_REC = [
    'orient'
]


class Separator(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, SEP_VALID, SEP_REC)
