from typing import List, Tuple

from build.objects.containers.container import Container

from ...buildConsts import intList_t, str_t, int_t, name_t, func_t, strList_t, nameList_t, color_t, bool_t

# WINDOW
FW_DEF_VALID: List[Tuple[str, str]] = [
    ('gridSize', intList_t),
    ('internalPadding', intList_t),
    ('border', str_t),
    ('borderWidth', int_t)
]
FW_DEF_REC: List[str] = ['gridSize']

WINDOW_STYLE = [
    ('background', color_t)
]

WINDOW_VALID_PARAM: List[Tuple[str, str]] = [
    ('title', str_t),
    ('size', intList_t),
    ('initOperation', func_t),
    ('exitOperation', func_t),
    ('loc', intList_t),
    ('menubar', name_t)
]

WINDOW_REC_PARAM: List[str] = [
    'title', 'size', 'initOperation', 'exitOperation',
]


class Window(Container):
    def __init__(self, name):
        super().__init__(name, WINDOW_VALID_PARAM + FW_DEF_VALID, WINDOW_REC_PARAM + FW_DEF_REC)


# FRAME
FRAME_VALID_PARAM: List[Tuple[str, str]] = [
    ('label', str_t),
    ('labelAnchor', str_t),
    ('labelWidget', name_t)
]

FRAME_STYLE = [
    ('background', color_t),
    ('labelDistance', int_t),
    ('labelOutside', bool_t),
    ('labelFont', str_t),
    ('labelTextColor', color_t)
]


class Frame(Container):
    def __init__(self, name: str):
        super().__init__(name, FRAME_VALID_PARAM, FW_DEF_REC)


# NOTEBOOK
NOTEBOOK_VALID_PARAM: List[Tuple[str, str]] = [
    ('tabNames', strList_t),
    ('tabs', nameList_t)
]

NOTEBOOK_REC_PARAM: List[str] = ['tabNames', 'tabs']


class Notebook(Container):
    def __init__(self, name):
        super().__init__(name, NOTEBOOK_VALID_PARAM, NOTEBOOK_REC_PARAM)

# TODO Canvas
# TODO PanedWindow
