from objects.datatypeConsts import str_t, name_t, color_t, bool_t, int_t
from objects.parseObject import ParseObject

LISTBOX_PARAM = [
    ('background', 'background', color_t),
    ('takeFocus', 'takefocus', bool_t),
    ('borderWidth', 'borderwidth', int_t),
    ('disabledTextColor', 'disabledforeground', color_t),
    ('font', 'font', str_t),
    ('textColor', 'foreground', color_t),
    ('inactiveHighlight', 'highlightbackground', color_t),
    ('activeHighlight', 'hightlightcolor', color_t),
    ('highlightWidth', 'hightlightthickness', int_t),
    ('justify', 'justify', str_t),
    ('relief', 'relief', str_t),
    ('selectedTextColor', 'selectforeground', color_t),
    ('selectedBG', 'selectbackground', color_t),
    ('selectBorderWidth', 'selectborderwidth', int_t),
    ('activeElementStyle', 'activestyle', str_t),
    ('height', 'height', int_t),
    ('width', 'width', int_t),
    ('listVariable', 'listvariable', name_t),
    ('selectionMode', 'selectmode', str_t),
    ('defaultState', 'state', str_t)
]

SCROLL = [
    ('xScroll', '', name_t),
    ('yScroll', '', name_t)
]

LISTBOX_REC = [
    'listVariable'
]


class Listbox(ParseObject):
    def __init__(self, name):
        super().__init__(name, LISTBOX_PARAM + SCROLL, LISTBOX_REC)
