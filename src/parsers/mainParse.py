# PARSER

from forgeExceptions import *
from objects.buildObject import BuildObject
from objects.interfaces import Container
from objects.parseObject import ParseObject
from objects.placement import Placement
from parsers.regexConsts import MAKE_CMD, SET_CMD, LOAD_CMD, DATATYPE_RE
from .objectTypeConsts import OBJECT_TYPES


def startParse(bo: BuildObject, infile: str):
    """
    Starts the parsing process

    :param bo: The build object to update
    :param infile: The input file path
    :return: The objects object created
    """

    # Strip and store all non-empty lines in file
    lines = []
    for line in open(infile, mode='r'):
        x = line.strip()
        # Skip line if commented out or empty
        if len(line) != 0 and line[0:2] != '//':
            lines.append(x)

    length = len(lines)
    idx = 0

    while idx < length:
        idx = parseNextCmd(lines, idx, bo)


def parseNextCmd(lines: List[str], idx: int, bo: BuildObject, parent: ParseObject = None) -> int:
    """
    Parses the next command

    :param bo: The master build object for gui
    :param lines: The input file lines
    :param idx: The index of the next command
    :param parent: The current parent object
    :return: The index of the next command
    """
    match = MAKE_CMD.fullmatch(lines[idx])
    if match is not None:
        return parseMakeCmd(lines, idx, bo, match)

    if parent is not None:
        match = SET_CMD.fullmatch(lines[idx])
        if match is not None:
            parseSetCmd(parent, match)
            return idx + 1

        match = LOAD_CMD.fullmatch(lines[idx])
        if match is not None:
            return parseLoadCmd(lines, idx, bo, parent, match)

    raise ParseException(lines[idx], 'Invalid command')


def parseMakeCmd(lines: List[str], idx: int, bo: BuildObject, match) -> int:
    """
    Parses a create/style command

    :param bo: The master build object
    :param match: The re match object of the command
    :param lines: The input file lines
    :param idx: The index of the next command
    :return: The new object and next index
    """

    # Extract command params
    cmd = match.group('cmd')
    datatype = match.group('datatype')
    name = match.group('name')

    # Create either object or style
    try:
        x = OBJECT_TYPES[datatype]
    except KeyError:
        raise InvalidDatatypeException(lines[idx], datatype)

    # Init Widget
    if cmd == 'create':
        obj = x[0](name)
        if obj is None:
            raise ParseException(lines[idx], 'Invalid datatype for this operation')
        bo.defineObject(obj)
    # Init Style
    else:
        obj = x[1](name)
        if obj is None:
            raise ParseException(lines[idx], 'Invalid datatype for this operation')
        bo.addStyle(obj)

    # Check for opening brace
    idx += 1
    if match.group('brace') is None:
        if lines[idx] != '{':
            raise ParseException(lines[idx], 'Missing opening curly bracket')
        else:
            idx += 1

    # Parse internals
    return parseObject(lines, idx, bo, obj)


def parseObject(lines: List[str], idx: int, bo: BuildObject, obj: ParseObject) -> int:
    """
    Parses an object.

    :param lines: The input file lines
    :param idx: The index of the first command inside object
    :param bo: The master build object
    :param obj: The object being parsed
    :return: The index of the next command after the end of object
    """
    # Parse all inner commands
    while idx < len(lines) and lines[idx] != '}':
        idx = parseNextCmd(lines, idx, bo, obj)

    # Check for closing brace
    if idx == len(lines):
        raise ParseException(lines[idx - 1], 'No closing curly bracket')

    # Increment past closing brace
    idx += 1

    return idx


def parseSetCmd(parent: ParseObject, match):
    """
    Parses a set command
    :param parent: The current object being parsed
    :param match: The re match of the command
    :return: None
    """
    key = match.group('key')
    value = match.group('value')

    validDatatype = parent.getDatatype(key)
    valueMatch = DATATYPE_RE[validDatatype].fullmatch(value)
    if valueMatch is None:
        raise InvalidParamTypeException(parent.name, key, validDatatype)

    parent.setParam(key, value)


def parseLoadCmd(lines, idx, bo, parent: ParseObject, match) -> int:
    """
    Parses a load command
    :param lines: The input file lines
    :param idx: The index of the command
    :param bo: The master build object
    :param parent: The parent being loaded into
    :param match: The re match of the command
    :return: The index of the next command
    """
    name = match.group('name')
    bo.claimObject(name, parent.name)

    placement = None
    read = False

    idx += 1

    if match.group('brace') is None:
        if lines[idx] == '{':
            idx += 1
            read = True
    else:
        read = True

    if read:
        placement = Placement(f'__{name}_Placement')
        idx = parseObject(lines, idx, bo, placement)


    if not isinstance(parent, Container):
        raise LoadException(parent.name, lines[idx])

    parent.load(name, placement=placement)
    return idx

