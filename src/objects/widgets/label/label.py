from objects.datatypeConsts import str_t, name_t, bool_t, intList_t, int_t
from objects.parseObject import Widget

LABEL_VALID = [
    ('padding', 'padding', intList_t),
    ('takeFocus', 'takefocus', bool_t),
    ('text', 'text', str_t),
    ('inputVariable', 'textvariable', name_t),
    ('width', 'width', int_t),
    ('justify', 'justify', str_t),
    ('defaultState', 'state', str_t),
    ('anchor', 'anchor', str_t),
    ('wrapLength', 'wraplength', int_t),
    ('acceleratorIdx', 'underline', int_t),
    ('relief', 'relief', str_t)
]

LABEL_REC = [
    # Intentionally left blank
]


class Label(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, LABEL_VALID, LABEL_REC)
