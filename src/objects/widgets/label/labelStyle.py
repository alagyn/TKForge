from objects.datatypeConsts import str_t, color_t
from objects.stateConsts import disabled_s, readonly_s
from objects.parseObject import Style

LABEL_STYLE_PARAM = [
    ('background', 'background', color_t),
    ('textColor', 'foreground', color_t),
    ('font', 'font', str_t),
    ('imageLoc', 'compound', str_t)
]

IMAGE = [
    ('image', 'image', str_t)
]

LABEL_STATES = [disabled_s, readonly_s]


class LabelStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, LABEL_STYLE_PARAM + IMAGE, LABEL_STATES)
