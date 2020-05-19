from objects.datatypeConsts import color_t, int_t, bool_t, str_t
from objects.parseObject import Style
from objects.stateConsts import disabled_s, readonly_s

FRAME_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('labelDistance', int_t),
    ('labelOutside', bool_t),
    ('labelFont', str_t),
    ('labelTextColor', color_t),
    ('darkColor', color_t),
    ('lightColor', color_t),
    ('relief', str_t),
    ('labelBG', color_t)
]

FRAME_STATES = [
    disabled_s, readonly_s
]


class FrameStyle(Style):
    def outputStyle(self):
        # TODO Frame style output
        pass

    def __init__(self, name):
        super().__init__(name, FRAME_STYLE, FRAME_STATES)
