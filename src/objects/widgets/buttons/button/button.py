from objects.datatypeConsts import str_t, name_t, bool_t, int_t
from objects.parseObject import Widget


BUTTON_PARAM = [
    ('imageLoc', str_t),  # Internal "compound"
    ('image', str_t),
    ('takeFocus', bool_t),
    ('defaultText', str_t),
    ('textVariable', name_t),
    ('underline', int_t),  # TODO button accelerator
    ('width', int_t),
    ('defaultState', str_t)
]

BUTTON_REC = []


class Button(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, BUTTON_PARAM, BUTTON_REC)

