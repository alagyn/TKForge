from objects.datatypeConsts import name_t, str_t, intList_t, int_t, strList_t
from objects.parseObject import Widget

PAGE_PARAM = [
    ('title', 'text', str_t),
    ('padding', 'padding', intList_t),
    ('sticky', 'sticky', str_t),
    ('defState', 'state', str_t),
    ('tabAccelerator', 'underline', int_t)
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
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


def __init__(self, name):
    super().__init__(name, PAGE_PARAM + IMAGE + DATA, PAGE_REC)
