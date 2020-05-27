from objects.datatypeConsts import color_t, str_t, bool_t, name_t, int_t
from objects.parseObject import ParseObject

# Textbox
TEXTBOX_VALID = [
    ('background', 'background', color_t),
    ('borderWidth', 'borderwidth', int_t),
    ('font', 'font', str_t),
    ('textColor', 'foreground', color_t),
    ('hightlightUnselected', 'highlightbackground', color_t),
    ('highlightSelected', 'highlightcolor', color_t),
    ('highlightWidth', 'highlightthickness', int_t),
    ('cursorBG', 'insertbackground', color_t),
    ('curserBorderWidth', 'insertborderwidth', int_t),
    ('cursorOnTime', 'insertontime', int_t),
    ('cursorOffTime', 'insertofftime', int_t),
    ('cursorWidth', 'insertwidth', int_t),
    ('xPad', 'padX', int_t),
    ('yPad', 'padY', int_t),
    ('relief', 'relief', str_t),
    ('selectBG', 'selectbackground', color_t),
    ('selectTextColor', 'selectforeground', color_t),
    ('selectBorderWidth', 'selectborderwidth', int_t),
    ('setGrid', 'setgrid', bool_t),
    ('defaultState', 'state', str_t),
    ('visibleStartIdx', 'startline', int_t),
    ('visibleEndIdx', 'endline', int_t),
    ('height', 'height', int_t),
    ('width', 'width', int_t),
    ('inactiveSelectBG', 'inactiveselectbackground', color_t),
    ('unfocussedCursor', 'insertunfocussed', str_t),
    ('wrap', 'wrap', str_t),
    ('tabStyle', 'tabstyle', str_t),
    ('undo', 'undo', bool_t),
    ('maxUndo', 'maxundo', int_t),
    ('aboveLineSpace', 'spacing1', int_t),
    ('betweenWrapSpace', 'spacing2', int_t),
    ('belowLineSpace', 'spacing3', int_t),
    ('text', 'text', str_t)
]

OTHER = [
    ('xScroll', '', name_t),
    ('yScroll', '', name_t)
]

TEXTBOX_REQ = [
    # Intentionally left blank
]


class TextBox(ParseObject):
    def __init__(self, name):
        super().__init__(name, TEXTBOX_VALID + OTHER, TEXTBOX_REQ)
