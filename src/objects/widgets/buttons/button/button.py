from objects.datatypeConsts import str_t, name_t, bool_t, int_t
from objects.parseObject import Widget


BUTTON_PARAM = [
    ('takeFocus', 'takefocus', bool_t),
    ('text', 'text', str_t),
    ('textVariable', 'textvariable', name_t),
    ('acceleratorIdx', 'underline', int_t),
    ('defaultState', 'state', str_t),
    ('defaultAction', 'default', bool_t)
]

BUTTON_REC = []


class Button(Widget):

    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, BUTTON_PARAM, BUTTON_REC)

