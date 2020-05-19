from objects.widgets.buttons.button.button import Button
from objects.widgets.buttons.selectionButton.checkButton import CheckButton
from objects.widgets.buttons.selectionButton.radioButton import RadioButton
from objects.widgets.canvas.canvas import Canvas
from objects.widgets.combobox.combobox import Combobox
from objects.widgets.entry.entry import Entry
from objects.widgets.framelike.frame.frame import Frame
from objects.widgets.framelike.notebook.notebook import Notebook
from objects.widgets.framelike.notebook.page import NotebookPage
from objects.widgets.framelike.panedFrame.pane import Pane
from objects.widgets.framelike.panedFrame.panedFrame import PanedFrame
from objects.widgets.framelike.window.window import Window
from objects.widgets.label.label import Label
from objects.widgets.listbox.listbox import Listbox
from objects.widgets.progressbar.progressbar import Progressbar
from objects.widgets.scalebar.scalebar import Scalebar
from objects.widgets.scrollbar.scrollbar import Scrollbar
from objects.widgets.separator.separator import Separator
from objects.widgets.spinbox.spinbox import Spinbox
from objects.widgets.text.text import TextBox
from objects.widgets.treeview.treeview import TreeView


OBJECT_TYPES = {
    'Button': Button,
    'CheckButton': CheckButton,
    'RadioButton': RadioButton,
    'Canvas': Canvas,
    'Combobox': Combobox,
    'Window': Window,
    'Frame': Frame,
    'PanedFrame': PanedFrame,
    'Pane': Pane,
    'Notebook': Notebook,
    'Page': NotebookPage,
    'Entry': Entry,
    'Label': Label,
    'Listbox': Listbox,
    # TODO Menus
    'Progressbar': Progressbar,
    'Scalebar': Scalebar,
    'Scrollbar': Scrollbar,
    'Separator': Separator,
    'Spinbox': Spinbox,
    'Textbox': TextBox,
    'Tree': TreeView
}

STYLE_TYPES = {

}

