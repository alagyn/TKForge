from objects.datatypeConsts import name_t, str_t, intList_t, int_t, strList_t
from objects.parseObject import Widget

PAGE_PARAM = [
    ('title', 'text', str_t),
    ('padding', 'padding', intList_t),
    ('sticky', 'sticky', str_t),
    ('defState', 'state', str_t),
    ('tabAccelerator', 'underline', int_t)  # TODO notebook accelerator
]

IMAGE = [
    ('imageSpec', '', strList_t)
]

DATA = [
    ('pageWidget', '', name_t)
]

PAGE_REC = [
    'title', 'pageWidget'
]


class NotebookPage(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, PAGE_PARAM + IMAGE + DATA, PAGE_REC)
