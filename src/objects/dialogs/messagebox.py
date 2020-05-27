from objects.datatypeConsts import str_t
from objects.parseObject import ParseObject

MESSAGE_PARAM = [
    ('type', '', str_t),
    ('title', '', str_t),
    ('icon', '', str_t),
    ('text', '', str_t),
    ('detailText', '', str_t),
    ('defaultButton', '', str_t)
]

MESSAGE_REC = [
    'type', 'text', 'title'
]


class MessageBox(ParseObject):
    def __init__(self, name):
        super().__init__(name, MESSAGE_PARAM, MESSAGE_REC)
