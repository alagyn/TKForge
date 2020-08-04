from typing import Dict, Tuple, Callable

from objects.parseObject import Widget, Style
from objects.widgets.buttons.button.button import Button
from objects.widgets.buttons.button.buttonStyle import ButtonStyle
from objects.widgets.buttons.selectionButton.checkButton import CheckButton
from objects.widgets.buttons.selectionButton.radioButton import RadioButton
from objects.widgets.buttons.selectionButton.selectionStyle import CheckButtonStyle, RadioButtonStyle
from objects.widgets.canvas.canvas import Canvas
from objects.widgets.combobox.combobox import Combobox
from objects.widgets.combobox.comboboxStyle import ComboboxStyle
from objects.widgets.entry.entry import Entry
from objects.widgets.entry.entryStyle import EntryStyle
from objects.widgets.framelike.frame.frame import Frame
from objects.widgets.framelike.frame.frameStyle import FrameStyle
from objects.widgets.framelike.notebook.notebook import Notebook
from objects.widgets.framelike.notebook.notebookStyle import NotebookStyle
from objects.widgets.framelike.notebook.page import NotebookPage
from objects.widgets.framelike.notebook.tabStyle import NotebookTabStyle
from objects.widgets.framelike.panedFrame.pane import Pane
from objects.widgets.framelike.panedFrame.panedFrame import PanedFrame
from objects.widgets.framelike.panedFrame.panedFrameStyle import PanedFrameStyle
from objects.widgets.framelike.window.window import Window
from objects.widgets.framelike.window.windowStyle import WindowStyle
from objects.widgets.label.label import Label
from objects.widgets.label.labelStyle import LabelStyle
from objects.widgets.listbox.listbox import Listbox
from objects.widgets.menus.menubar.menuList import MenuList
from objects.widgets.menus.menubar.menubar import MenuBar
from objects.widgets.progressbar.progressbar import Progressbar
from objects.widgets.progressbar.progressbarStyle import ProgressbarStyle
from objects.widgets.scalebar.scalebar import Scalebar
from objects.widgets.scalebar.scalebarStyle import ScalebarStyle
from objects.widgets.scrollbar.scrollbar import Scrollbar
from objects.widgets.scrollbar.scrollbarStyle import ScrollbarStyle
from objects.widgets.separator.separator import Separator
from objects.widgets.separator.separatorStyle import SeparatorStyle
from objects.widgets.spinbox.spinbox import Spinbox
from objects.widgets.spinbox.spinboxStyle import SpinboxStyle
from objects.widgets.text.text import TextBox
from objects.widgets.treeview.treeview import TreeView
from objects.widgets.treeview.treeviewStyle import TreeViewStyle

OBJECT_TYPES: Dict[str, Tuple[Callable[[str], Widget], Callable[[str], Style]]] = {
    'Button': (Button, ButtonStyle),
    'CheckButton': (CheckButton, CheckButtonStyle),
    'RadioButton': (RadioButton, RadioButtonStyle),
    'Canvas': (Canvas, None),
    'Combobox': (Combobox, ComboboxStyle),
    'Window': (Window, WindowStyle),
    'Frame': (Frame, FrameStyle),
    'PanedFrame': (PanedFrame, PanedFrameStyle),
    'Pane': (Pane, None),
    'Notebook': (Notebook, NotebookStyle),
    'NoteBookTab': (None, NotebookTabStyle),
    'Page': (NotebookPage, None),
    'Entry': (Entry, EntryStyle),
    'Label': (Label, LabelStyle),
    'Listbox': (Listbox, None),
    'Menubar': (MenuBar, None),
    'MenuList': (MenuList, None),
    'Progressbar': (Progressbar, ProgressbarStyle),
    'Scalebar': (Scalebar, ScalebarStyle),
    'Scrollbar': (Scrollbar, ScrollbarStyle),
    'Separator': (Separator, SeparatorStyle),
    'Spinbox': (Spinbox, SpinboxStyle),
    'Textbox': (TextBox, None),
    'Tree': (TreeView, TreeViewStyle)
}
