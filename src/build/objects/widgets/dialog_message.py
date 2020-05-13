from ..parseObject import ParseObject
from ...buildConsts import str_t, int_t, strList_t

DIALOG_PARAM = [
    ('title', str_t),
    ('text', str_t),
    ('defaultButtonIdx', int_t),
    ('buttonLabels', strList_t),
    ('icon', str_t)
]

DIALOG_REC = [
    'title', 'buttonLabels'
]


class CustomDialog(ParseObject):
    def __init__(self, name):
        super().__init__(name, DIALOG_PARAM, DIALOG_REC)


MESSAGE_PARAM = [
    ('type', str_t),
    ('title', str_t),
    ('icon', str_t),
    ('text', str_t),
    ('detailText', str_t),
    ('defaultButton', str_t)
]

MESSAGE_REC = [
    'type', 'text', 'title'
]


class MessageBox(ParseObject):
    def __init__(self, name):
        super().__init__(name, MESSAGE_PARAM, MESSAGE_REC)
