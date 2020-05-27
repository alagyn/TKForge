from objects.datatypeConsts import color_t, str_t
from objects.parseObject import Style

WINDOW_STYLE = [
    ('background', 'background', color_t),
    ('relief', 'relief', str_t)
]


class WindowStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, WINDOW_STYLE, [])
