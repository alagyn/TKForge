import re

from objects.datatypeConsts import *

# Commands
MAKE_CMD = re.compile(r'(?P<cmd>style|create) +'
                      r'(?P<datatype>[A-Z][a-zA-Z]*)? +'
                      r'(?P<name>[a-zA-Z]\w+) *: *(?P<brace>[{])?')

SET_CMD = re.compile(r'set +'
                     r'(?P<key>[a-zA-Z]+) *: +'
                     r'(?P<value>[\w,\[\] "#.]+)')

LOAD_CMD = re.compile(r'load +'
                      r'(?P<name>[a-zA-Z]\w*) *: (?P<brace>[{])?')

# Param Datatypes
INT_RE = re.compile(r'[0-9]+')
FLOAT_RE = re.compile(r'[0-9]+([.][0-9]*)?')
STR_RE = re.compile(r'"[\w\s]*"')
NAME_RE = re.compile(r'\w+')
BOOL_RE = re.compile(r'(1)|(0)|(true)|(false)')
COLOR_RE = re.compile(r'("\w+")|(#[0-9a-fA-F]{3})')
INTLIST_RE = re.compile(r'\[ *[0-9]+( *, *[0-9]+)* *\]')
FLOATLIST_RE = re.compile(r'\[ *([0-9]+([.][0-9]*)?)( *, [0-9]+([.][0-9]*)?)* *\]')
STRLIST_RE = re.compile(r'\[ *"[\w\s]*"( *, *"[\w\s]*")* *\]')

DATATYPE_RE = {
    int_t: INT_RE,
    float_t: FLOAT_RE,
    str_t: STR_RE,
    name_t: NAME_RE,
    bool_t: BOOL_RE,
    color_t: COLOR_RE,
    intList_t: INTLIST_RE,
    floatList_t: FLOATLIST_RE,
    strList_t: STRLIST_RE
}