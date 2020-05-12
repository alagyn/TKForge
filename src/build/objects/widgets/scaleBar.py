from ..parseObject import Widget, Style

from ...buildConsts import float_t, func_t, name_t, str_t, int_t, color_t, bool_t, active_s

SCALEBAR_VALID = [
    ('takeFocus', bool_t),
    ('bottomValue', float_t),
    ('topValue', float_t),
    ('command', func_t),
    ('variable', name_t),
    ('orient', str_t),
    ('length', int_t),
    ('defaultValue', float_t)
]

SCALEBAR_REC = [
    'variable', 'orient', 'bottomValue', 'topValue'
]


class Scalebar(Widget):
    def __init__(self, name):
        super().__init__(name, SCALEBAR_VALID, SCALEBAR_REC)


SCALE_STYLE_STATES = [active_s]

SCALE_STYLE_PARAM = [
    ('background', color_t),
    ('borderWidth', int_t),
    ('darkColor', color_t),
    ('grooveWidth', int_t),
    ('lightColor', color_t),
    ('sliderWidth', int_t),
    ('troughColor', color_t),
    ('troughRelief', str_t)
]


class ScalebarStyle(Style):
    def __init__(self, name):
        super().__init__(name, SCALE_STYLE_PARAM, SCALE_STYLE_STATES)
