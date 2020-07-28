from objects.datatypeConsts import color_t, str_t, int_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import disabled_s, selected_s

TREE_STYLE = [
    ('background', 'background', color_t),
    ('fieldBG', 'fieldbackground', color_t),
    ('font', 'font', str_t),
    ('textColor', 'foreground', color_t),
    ('rowHeight', 'rowheight', int_t)
]

HEADING = [
    ('headingBG', 'background', color_t),
    ('headingFont', 'font', str_t),
    ('headingRelief', 'relief', str_t)
]

ITEM = [
    ('indicatorMargins', 'indicatormargins', intList_t),
    ('indicatorSize', 'indicatorsize', int_t),
    ('itemTextColor', 'foreground', color_t),
    ('itemPadding', 'padding', intList_t),
]

CELL = [
    ('cellPadding', 'padding', intList_t)
]

TREE_STATES = [
    disabled_s, selected_s
]


class TreeViewStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, TREE_STYLE + HEADING + ITEM + CELL, TREE_STATES)
