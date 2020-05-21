from objects.datatypeConsts import color_t, intList_t, str_t, name_t
from objects.parseObject import Style

NOTEBOOK_STYLE = [
    ('background', 'background', color_t),
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('textColor', 'foreground', color_t),  # no effect?
    ('lightColor', 'lightcolor', color_t),
    ('externalPadding', 'padding', intList_t),
    ('tabPadding', 'tabmargins', intList_t),
    ('tabPosition', 'tabposition', str_t)  # compass direction i.e. n,ne,s,sw

]

TAB = [
    ('tabStyle', '', name_t)
]


class NotebookStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, NOTEBOOK_STYLE + TAB, [])
