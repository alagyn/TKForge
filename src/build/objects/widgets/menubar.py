from ..parseObject import Widget

from ...buildConsts import nameList_t

# TODO menubar style

MENU_BAR_VALID = [
    ('menuLists', nameList_t)
]

MENU_BAR_REQ = [
    'menuLists'
]


class MenuBar(Widget):
    def __init__(self, name):
        super().__init__(name, MENU_BAR_VALID, MENU_BAR_REQ)


# MenuList

MENU_LIST_VALID = [
    ('listItems', nameList_t)
]

MENU_LIST_REQ = [
    'listItems'
]


class MenuList(Widget):
    def __init__(self, name):
        super().__init__(name, MENU_LIST_VALID, MENU_LIST_REQ)

# TODO accelerator keys?
