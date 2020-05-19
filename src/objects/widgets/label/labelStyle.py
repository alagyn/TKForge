from objects.datatypeConsts import str_t, color_t
from objects.stateConsts import disabled_s, readonly_s
from objects.parseObject import Style

LABEL_STYLE_PARAM = [
    ('background', color_t),
    ('textColor', color_t),
    ('font', str_t)
]

LABEL_STATES = [disabled_s, readonly_s]


class LabelStyle(Style):
    def outputStyle(self):
        pass

    def __init__(self, name):
        super().__init__(name, LABEL_STYLE_PARAM, LABEL_STATES)
