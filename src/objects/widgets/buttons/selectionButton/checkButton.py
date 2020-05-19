from objects.datatypeConsts import str_t, name_t, bool_t, int_t, func_t
from objects.parseObject import Widget

CHECK_V = [
    ('image', str_t),
    ('takeFocus', bool_t),
    ('text', str_t),
    ('textVariable', name_t),
    ('underline', int_t),  # TODO check button accelerator
    ('width', int_t),
    ('command', func_t),
    ('onValue', str_t),
    ('offValue', str_t),
    ('outputVariable', name_t)
]

CHECK_REC = [
    'onValue', 'offValue', 'outputVariable', 'text'
]


class CheckButton(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, CHECK_V, CHECK_REC)
