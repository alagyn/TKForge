from typing import Callable, List, Tuple

from objects.parseObject import ParseObject

# Datatype for object parsing functions
ParseFunc = Callable[[str, List[str], int], Tuple[ParseObject, int]]


RESERVED_WORDS = {'create', 'load', 'set', 'style'}
RESERVED_NAMES = {'MENU_SEPARATOR', 'SIZE_GRIP', 'DEFAULT'}
