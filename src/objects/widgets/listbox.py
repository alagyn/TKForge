from objects.datatypeConsts import str_t, name_t, color_t, bool_t, int_t
from objects.parseObject import ParseObject

LISTBOX_PARAM = [
    ('background', color_t),
    ('takeFocus', bool_t),
    ('borderWidth', int_t),
    ('disabledTextColor', color_t),
    ('font', str_t),
    ('textColor', color_t),
    ('inactiveHighlight', color_t),
    ('activeHighlight', color_t),
    ('highlightWidth', int_t),
    ('justify', str_t),
    ('relief', str_t),
    ('selectedTextColor', color_t),
    ('selectedBG', color_t),
    ('xScroll', name_t),
    ('yScroll', name_t),
    ('activeElementStyle', str_t),
    ('height', int_t),
    ('width', int_t),
    ('listVariable', name_t),
    ('selectionMode', str_t),
    ('defaultState', str_t)
]

LISTBOX_REC = [
    'listVariable'
]


class Listbox(ParseObject):
    def __init__(self, name):
        super().__init__(name, LISTBOX_PARAM, LISTBOX_REC)
