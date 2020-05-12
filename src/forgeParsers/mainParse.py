# PARSER
import re
from build.buildObject import BuildObject
from typing import List
from exceptions.forgeException import ParseException

from forgeParsers.parseConsts import PARSERS

# REGEX
IMPORT = re.compile(r'import [\w.]+(, [\w.]+)*|from [\w.]+(, [\w.]+)* import [\w.]+(, [\w.]+)*')
TOP_LEVEL_HEADER = re.compile(r'create (\w+) (\w+):')


def startParse(infile: str) -> BuildObject:
    """
    Starts the parsing process

    :param infile: The input file path
    :return: The build object created
    """
    # TODO save imported function names?
    # TODO save which names have been loaded
    #   prevent loading 1 object onto multiple containers?

    # TODO skip commented lines

    bo = BuildObject()

    # Strip and store all non-empty lines in file
    lines = []
    for line in open(infile, mode='r'):
        x = line.strip()
        lines.append(x)

    # Parse the import section, returns starting index
    idx = parseImports(bo, lines)
    # Parse the rest of the file
    length = len(lines)
    while idx < length:
        idx = toplevelParse(bo, lines, idx)

    return bo


def parseImports(bo: BuildObject, lines: List[str]) -> int:
    """
    Parses the Python imports at the top of forge file

    :param bo: The current build object
    :param lines: List of all stripped input file lines
    :return: The starting index for global forgeParsers
    """

    idx = 0
    for line in lines:
        if line != '':
            match = IMPORT.fullmatch(line)
            if match is None:
                break
            idx += 1
            bo.imports.append(line)

    return idx


def toplevelParse(bo: BuildObject, lines: List[str], idx: int) -> int:
    """
    Parses the next toplevel block

    :param bo: The current build object
    :param lines: The input file
    :param idx: The current index
    :return: The next index to parse, after end of block
    """
    # Skip blank lines
    while idx < len(lines) and lines[idx] == '':
        idx += 1

    # If EOF, return
    if idx >= len(lines):
        return idx

    # Else parse block
    match = TOP_LEVEL_HEADER.fullmatch(lines[idx])

    # RegEx fail
    if match is None:
        raise ParseException(lines[idx], idx, 'Invalid top level header')

    # Extract variables
    cmd, datatype, name = match.group(1, 2, 3)

    # The only valid toplevel command
    if cmd != 'create':
        raise ParseException(lines[idx], idx, 'Invalid top level command')

    if name in bo.defined:
        raise ParseException(lines[idx], idx, 'Name already defined')

    # Try to retrieve parser
    try:
        parser = PARSERS[datatype]
    except KeyError:
        # Invalid key, I.E. invalid datatype
        raise ParseException(lines[idx], idx, 'Invalid datatype')

    # Parse object
    idx += 1
    newObj, idx = parser(name, lines, idx)

    # Append object to build
    bo.addObject(newObj)

    return idx
