from objects.datatypeConsts import strList_t, name_t, str_t, bool_t, int_t
from objects.parseObject import Widget



COMBO_BOX_VALID = [
    ('takeFocus', bool_t),
    ('justify', str_t),
    ('defaultState', str_t),
    ('outputVariable', name_t),
    ('values', strList_t),
    ('width', int_t),
    ('height', int_t)

]

COMBO_BOX_REC = [
    'values', 'outputVariable'
]


class Combobox(Widget):
    def __init__(self, name):
        super().__init__(name, COMBO_BOX_VALID, COMBO_BOX_REC)
