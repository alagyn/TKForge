from objects.datatypeConsts import name_t, str_t, intList_t, int_t
from objects.parseObject import Widget

PAGE_PARAM = [
    ('pageWidget', name_t),
    ('title', str_t),
    ('image', str_t),
    ('padding', intList_t),
    ('sticky', str_t),
    ('defState', str_t),
    ('imageLoc', str_t),
    ('textUnderline', int_t)  # TODO notebook accelerator
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
        super().__init__(name, PAGE_PARAM, PAGE_REC)
