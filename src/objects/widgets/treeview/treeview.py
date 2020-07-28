from objects.datatypeConsts import bool_t, intList_t, int_t, name_t, str_t, strList_t
from objects.parseObject import Widget

TREE_PARAM = [
    ('internalPadding', 'padding', intList_t),
    ('takeFocus', 'takefocus', bool_t),
    ('columnNames', 'columns', strList_t),
    ('displayColumns', 'displaycolumns', strList_t),
    ('rowsVisible', 'height', int_t),
    ('selectMode', 'selectmode', str_t),
    ('viewMode', 'show', strList_t)
]

OTHER = [
    ('xScroll', '', name_t),
    ('yScroll', '', name_t)
]

TREE_REC = [
    'columnNames'
]


class TreeView(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, TREE_PARAM + OTHER, TREE_REC)
