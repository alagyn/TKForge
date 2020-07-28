from objects.datatypeConsts import strList_t, name_t, str_t, bool_t, int_t
from objects.parseObject import Widget

COMBO_BOX_VALID = [
    ('takeFocus', 'takefocus', bool_t),
    ('justify', 'justify', str_t),
    ('defaultState', 'state', str_t),
    ('outputVariable', 'textvariable', name_t),
    ('values', 'values', strList_t),
    ('width', 'width', int_t),
    ('visibleRows', 'height', int_t)

]

COMBO_BOX_REC = [
    'values', 'outputVariable'
]


class Combobox(Widget):
    def outputConfig(self):
        pass

    def outputPost(self):
        pass

    def outputCommand(self):
        pass

    def outputInit(self):
        pass


    def __init__(self, name):
        super().__init__(name, COMBO_BOX_VALID, COMBO_BOX_REC, 'Combobox')
