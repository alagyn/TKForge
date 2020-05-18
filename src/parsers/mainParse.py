# PARSER
import re
from objects.buildObject import BuildObject
from typing import List, Tuple
from forgeExceptions import *
from objects.parseObject import ParseObject
from .objectTypeConsts import OBJECT_TYPES

# REGEX
OBJECT_HEADER = re.compile(r'create +'
                           r'(?P<datatype>[A-Z][a-zA-Z]*)? +'
                           r'(?P<name>[a-zA-Z0-9]+): *(?P<brace>[{])?')


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
        obj, idx = parseNextObject(lines, idx)
        # TODO add toplevel to BO


def parseNextObject(lines: List[str], idx: int) -> Tuple[ParseObject, int]:
    """
    Parses the next object
    :param lines: The input file lines
    :param idx: The index of the next command
    :return: The new object and next index
    """
    match = OBJECT_HEADER.fullmatch(lines[idx])
    if match is None:
        raise ParseException(lines[idx], 'Invalid object header')

    name = match.group('name')
    datatype = match.group('datatype')

    try:
        obj = OBJECT_TYPES[datatype](name)
    except KeyError:
        raise InvalidDatatypeException(lines[idx], datatype)

    idx += 1

    return (obj, idx)
