from objects.datatypeConsts import str_t, strList_t, int_t
from objects.parseObject import ParseObject


DIALOG_PARAM = [
    ('title', '', str_t),
    ('text', '', str_t),
    ('defaultButtonIdx', '', int_t),
    ('buttonLabels', '', strList_t),
    ('icon', '', str_t)
]

DIALOG_REC = [
    'title', 'buttonLabels'
]


class Dialog(ParseObject):
    def __init__(self, name):
        super().__init__(name, DIALOG_PARAM, DIALOG_REC, '')

