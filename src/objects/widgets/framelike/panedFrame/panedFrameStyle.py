from objects.datatypeConsts import color_t, int_t, str_t
from objects.parseObject import Style

PANED_STYLE = [
    ('background', color_t),
    ('sashBG', color_t),
    ('sashBorderColor', color_t),
    ('gripCount', int_t),
    ('handlePadding', int_t),
    ('handleSize', int_t),
    ('lightColor', color_t),
    ('sashPadding', int_t),
    ('sashRelief', str_t),
    ('sashThickness', int_t)
]


class PanedFrameStyle(Style):
    # TODO PanedFrameStyle output
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, PANED_STYLE, [])
