from objects.datatypeConsts import str_t, name_t, bool_t, intList_t, int_t
from objects.parseObject import Widget

LABEL_VALID = [
    ('imageLoc', str_t),
    ('image', str_t),
    ('padding', intList_t),
    ('takeFocus', bool_t),
    ('text', str_t),
    ('inputVariable', name_t),
    ('width', int_t),
    ('justify', str_t),
    ('defaultState', str_t),
    ('anchor', str_t),
    ('wrapLength', int_t),
    ('underline', int_t),  # TODO label accelerator?
    ('relief', str_t)
]

LABEL_REC = [
    # Intentionally left blank
]


class Label(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, LABEL_VALID, LABEL_REC)

