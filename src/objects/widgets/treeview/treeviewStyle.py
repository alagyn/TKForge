from objects.datatypeConsts import color_t, str_t, int_t, intList_t
from objects.parseObject import Style
from objects.stateConsts import disabled_s, selected_s

TREE_STYLE = [
    ('background', color_t),
    ('fieldBG', color_t),
    ('font', str_t),
    ('textColor', color_t),
    ('rowHeight', int_t),
    ('headingBG', color_t),
    ('indicatorMargins', intList_t),
    ('indicatorSize', int_t),
    ('itemTextColor', color_t),
    ('itemPadding', intList_t),
    ('cellPadding', intList_t)
]

TREE_STATES = [
    disabled_s, selected_s
]


class TreeViewStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, TREE_STYLE, TREE_STATES)
