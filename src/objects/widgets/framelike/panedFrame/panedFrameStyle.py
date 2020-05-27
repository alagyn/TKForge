from objects.datatypeConsts import color_t, int_t, str_t
from objects.parseObject import Style

PANED_STYLE = [
    ('background', 'background', color_t)
]

SASH_STYLE = [
    ('sashBG', 'background', color_t),
    ('sashBorderColor', 'bordercolor', color_t),
    ('gripCount', 'gripcount', int_t),
    ('handlePadding', 'handlepad', int_t),
    ('handleSize', 'handlesize', int_t),
    ('lightColor', 'lightcolor', color_t),
    ('sashPadding', 'sashpad', int_t),
    ('sashRelief', 'sashrelief', str_t),
    ('sashThickness', 'sashthickness', int_t)
]


class PanedFrameStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, PANED_STYLE + SASH_STYLE, [])
