from objects.datatypeConsts import str_t, name_t, bool_t, int_t
from objects.parseObject import Widget

CHECK_V = [
    ('takeFocus', 'takefocus', bool_t),
    ('text', 'text', str_t),
    ('textVariable', 'textvariable', name_t),
    ('acceleratorIdx', 'underline', int_t),
    ('width', 'width', int_t),
    ('onValue', 'onvalue', str_t),
    ('offValue', 'offvalue', str_t),
    ('outputVariable', 'variable', name_t)
]

COMMAND = [
    ('command', '', bool_t)
]

CHECK_REC = [
    'onValue', 'offValue', 'outputVariable'
]


class CheckButton(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, CHECK_V + COMMAND, CHECK_REC)
