from typing import Callable, List, Dict, Tuple
from parsers.objParsers import FrameLikeParse
from objects.parseObject import ParseObject

# Datatype for object parsing functions
ParseFunc = Callable[[str, List[str], int], Tuple[ParseObject, int]]

# Dict of parse funcs
PARSERS: Dict[str, ParseFunc] = {
    'Window': FrameLikeParse.parseWindow,
    'Frame': FrameLikeParse.parseFrame,
    'Notebook': FrameLikeParse.parseNotebook,
    'PanedFrame': FrameLikeParse.parsePanedFrame
}

RESERVED_WORDS = {'create', 'load', 'set', 'style'}
RESERVED_NAMES = {'MENU_SEPARATOR', 'SIZE_GRIP', 'DEFAULT'}
