from typing import List, Tuple, Dict

from objects.datatypeConsts import str_t, color_t, name_t, float_t, nameList_t, bool_t, intList_t, func_t, \
    floatList_t, int_t
from objects.stateConsts import disabled_s, readonly_s, active_s, selected_s
from objects.parseObject import Style, Widget
from objects.placement import Placement

# TODO break containers into separate files
CONTAINER_VALID: List[Tuple[str, str]] = [
    ('internalPadding', intList_t),
    ('borderWidth', int_t),
    ('takeFocus', bool_t),
    ('rowWeights', floatList_t),
    ('colWeights', floatList_t)
]


class Container(Widget):
    def __init__(self, name: str, validParams: List[Tuple[str, str]], requiredParams: List[str]):
        super().__init__(name, validParams + CONTAINER_VALID, requiredParams)

        self.objects: Dict[Widget, Placement] = {}

    def loadObj(self, obj: Widget, placement: Placement):
        if obj not in self.objects:
            self.objects[obj] = placement


# WINDOW
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
        super().__init__(name, WINDOW_VALID_PARAM, WINDOW_REC_PARAM)


WINDOW_STYLE = [
    ('background', color_t),
    ('relief', str_t)
]


class WindowStyle(Style):
    def __init__(self, name):
        super().__init__(name, WINDOW_STYLE, [])


# FRAME
FRAME_VALID_PARAM: List[Tuple[str, str]] = [
    ('label', str_t),
    ('labelAnchor', str_t),
    ('labelWidget', name_t),
    ('underline', int_t),  # TODO Labelframe accelerator
    ('takeFocus', bool_t)
]

FRAME_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('labelDistance', int_t),
    ('labelOutside', bool_t),
    ('labelFont', str_t),
    ('labelTextColor', color_t),
    ('darkColor', color_t),
    ('lightColor', color_t),
    ('relief', str_t),
    ('labelBG', color_t)
]

FRAME_STATES = [
    disabled_s, readonly_s
]


class Frame(Container):
    def __init__(self, name: str):
        super().__init__(name, FRAME_VALID_PARAM, [])


class FrameStyle(Style):
    def __init__(self, name):
        super().__init__(name, FRAME_STYLE, FRAME_STATES)


# NOTEBOOK
NOTEBOOK_VALID_PARAM: List[Tuple[str, str]] = [
    ('tabs', nameList_t),
    ('takeFocus', bool_t)
]

NOTEBOOK_REC_PARAM: List[str] = ['tabs']

NOTEBOOK_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('darkColor', color_t),
    ('textColor', color_t),  # Internal foreground, no effect?
    ('lightColor', color_t),
    ('externalPadding', intList_t),
    ('tabPadding', intList_t),
    ('tabPosition', str_t),  # compass direction i.e. n,ne,s,sw
    ('tabStyle', name_t)
]


class Notebook(Container):
    def __init__(self, name):
        super().__init__(name, NOTEBOOK_VALID_PARAM, NOTEBOOK_REC_PARAM)


class NotebookStyle(Style):
    def __init__(self, name):
        super().__init__(name, NOTEBOOK_STYLE, [])


TAB_STYLE = [
    ('background', color_t),
    ('borderColor', color_t),
    ('expand', intList_t),
    ('font', str_t),
    ('textColor', color_t),
    ('padding', intList_t)
]

TAB_STATES = [
    active_s, disabled_s, selected_s
]


class TabStyle(Style):
    def __init__(self, name):
        super().__init__(name, TAB_STYLE, TAB_STATES)


PAGE_PARAM = [
    ('pageWidget', name_t),
    ('title', str_t),
    ('image', str_t),
    ('padding', intList_t),
    ('sticky', str_t),
    ('defState', str_t),
    ('imageLoc', str_t),
    ('textUnderline', int_t)  # TODO notebook accelerator
]

PAGE_REC = [
    'title', 'pageWidget'
]


class NotebookPage(Widget):
    def __init__(self, name):
        super().__init__(name, PAGE_PARAM, PAGE_REC)


PANED_FRAME_PARAM = [
    ('takeFocus', bool_t),
    ('orient', str_t),
    ('panes', nameList_t)
]

PANED_FRAME_REC = [
    'orient', 'panes'
]


class PanedFrame(Container):
    def __init__(self, name):
        super().__init__(name, PANED_FRAME_PARAM, PANED_FRAME_REC)


PANE_PARAM = [
    ('weight', float_t),
    ('widget', name_t)
]

PANE_REC = ['widget']


class Pane(Widget):
    def __init__(self, name):
        super().__init__(name, PANE_PARAM, PANE_REC)


PANED_STYLE = [
    ('background', color_t),
    ('sashBG', color_t),
    ('sashBorderColor', color_t),
    ('gripCount', int_t),
    ('handlePadding', int_t),
    ('handleSize', int_t),
    ('lightColor', color_t),
    ('sashPadding', int_t),
    ('sashRelief', str_t),
    ('sashThickness', int_t)
]


class PanedFrameStyle(Style):
    def __init__(self, name):
        super().__init__(name, PANED_STYLE, [])
# TODO Canvas