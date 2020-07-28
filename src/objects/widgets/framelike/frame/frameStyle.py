from objects.datatypeConsts import color_t, int_t, bool_t, str_t
from objects.parseObject import Style
from objects.stateConsts import disabled_s, readonly_s

FRAME_STYLE = [
    ('background', 'background', color_t),
    ('relief', str_t)
]

LABEL_FRAME = [
    ('borderColor', 'bordercolor', color_t),
    ('darkColor', 'darkcolor', color_t),
    ('lightColor', 'lightcolor', color_t),
    ('labelDistance', 'labelmargins', int_t),
    ('labelOutside', 'labeloutside', bool_t),
]

LABEL = [
    ('labelFont', 'font', str_t),
    ('labelTextColor', 'foreground', color_t),
    ('labelBG', 'background', color_t)
]

FRAME_STATES = [
    disabled_s, readonly_s
]


class FrameStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, FRAME_STYLE + LABEL_FRAME + LABEL, FRAME_STATES)
