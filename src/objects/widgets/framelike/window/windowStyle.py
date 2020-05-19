from objects.datatypeConsts import color_t, str_t
from objects.parseObject import Style

WINDOW_STYLE = [
    ('background', color_t),
    ('relief', str_t)
]


class WindowStyle(Style):
    # TODO WindowStyle output
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, WINDOW_STYLE, [])
