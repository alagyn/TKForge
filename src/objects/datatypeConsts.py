from typing import Dict

intList_t = 'int_list'
floatList_t = 'float_list'
strList_t = 'string_list'
nameList_t = 'item_name_list'
funcList_t = 'func_list'
boolList_t = 'boolean_list'
int_t = 'integer'
float_t = 'float'
str_t = 'string'
func_t = 'function'
name_t = 'item_name'
bool_t = 'boolean'
color_t = 'color'

DATA_NAMES = [intList_t, floatList_t, strList_t, nameList_t, funcList_t,
              int_t, float_t, str_t, func_t, name_t, bool_t, color_t, boolList_t]

# TODO remove TO_ENUM/NAME?
TO_ENUM: Dict[str, int] = {k: v for k, v in zip(DATA_NAMES, range(0, len(DATA_NAMES)))}
TO_NAME: Dict[int, str] = {v: k for k, v in TO_ENUM.items()}

if __name__ == '__main__':
    print(TO_ENUM)