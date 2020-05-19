from objects.datatypeConsts import bool_t, intList_t, int_t, name_t, str_t, strList_t
from objects.parseObject import Widget

TREE_PARAM = [
    ('internalPadding', intList_t),
    ('takeFocus', bool_t),
    ('xScroll', name_t),
    ('yScroll', name_t),
    ('columnNames', strList_t),
    ('rowsVisible', int_t),
    ('selectMode', str_t),
    ('viewMode', strList_t)  # internal "show"
]

TREE_REC = [
    'columnNames'
]


class TreeView(Widget):
    def declaration(self):
        pass

    def outputParams(self):
        pass

    def postInit(self):
        pass

    def __init__(self, name):
        super().__init__(name, TREE_PARAM, TREE_REC)
