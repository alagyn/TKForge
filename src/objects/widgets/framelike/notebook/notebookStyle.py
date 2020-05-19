from objects.datatypeConsts import color_t, intList_t, str_t, name_t
from objects.parseObject import Style

NOTEBOOK_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('textColor', color_t),  # Internal foreground, no effect?
    ('lightColor', color_t),
    ('externalPadding', intList_t),
    ('tabPadding', intList_t),
    ('tabPosition', str_t),  # compass direction i.e. n,ne,s,sw
    ('tabStyle', name_t)
]


class NotebookStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, NOTEBOOK_STYLE, [])
