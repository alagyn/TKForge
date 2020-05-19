# PARSER
import re
from objects.buildObject import BuildObject
from typing import List, Tuple
from forgeExceptions import *
from objects.parseObject import ParseObject
from .objectTypeConsts import OBJECT_TYPES, STYLE_TYPES

# REGEX

MAKE_CMD = re.compile(r'(?P<cmd>style|create) +'
                      r'(?P<datatype>[A-Z][a-zA-Z]*)? +'
                      r'(?P<name>[a-zA-Z]\w+) *: *(?P<brace>[{])?')

SET_CMD = re.compile(r'set +'
                     r'(?P<param>[a-zA-Z]+) *: +'
                     r'(?P<data>[\w,\[\] "#.]+)')

LOAD_CMD = re.compile(r'load +'
                      r'(?P<name>[a-zA-Z]\w*) *: (?P<brace>[{])?')


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
        # TODO add toplevel to BO


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
        return parseNextObject(lines, idx, bo, match)

    if parent is not None:
        match = SET_CMD.fullmatch(lines[idx])
        if match is not None:
            # TODO set cmd
            return idx

        match = LOAD_CMD.fullmatch(lines[idx])
        if match is not None:
            # TODO load cmd
            return idx


def parseNextObject(lines: List[str], idx: int, bo: BuildObject, match) \
        -> int:
    """
    Parses the next object

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
    if cmd == 'create':
        try:
            obj = OBJECT_TYPES[datatype](name)
        except KeyError:
            raise InvalidDatatypeException(lines[idx], datatype)

        # Add object to BO
        bo.defineObject(obj)

    else:
        try:
            obj = STYLE_TYPES[datatype](name)
        except KeyError:
            raise InvalidDatatypeException(lines[idx], datatype)

        # Add style to BO
        bo.addStyle(obj)

    # Check for opening brace
    idx += 1
    if match.group('brace') is None:
        if lines[idx] != '{':
            raise ParseException(lines[idx], 'Missing opening curly bracket')
        else:
            idx += 1

    # Parse all inner commands
    while idx < len(lines) and lines[idx] != '}':
        idx = parseNextCmd(lines, idx, bo, obj)

    # Check for closing brace
    if idx == len(lines):
        raise ParseException(lines[idx - 1], 'No closing curly bracket')

    # Increment past closing brace
    idx += 1

    return idx
