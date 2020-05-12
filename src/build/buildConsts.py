from typing import Dict

intList_t = 'int_list'
floatList = 'float_list'
strList = 'string_list'
nameList = 'item_name_list'
funcList = 'func_list'
int_t = 'integer'
float_t = 'float'
str_t = 'string'
func_t = 'function'
name_t = 'item_name'
bool_t = 'boolean'
color_t = 'color'

DATA_NAMES = [intList_t, floatList, strList, nameList, funcList,
              int_t, float_t, str_t, func_t, name_t, bool_t, color_t]

# States
active_s = 'active'
disabled_s = 'disabled'
pressed_s = 'pressed'
focus_s = 'focus'
selected_s = 'selected'
background_s = 'background'
readonly_s = 'readonly'
alternate_s = 'alternate'
invalid_s = 'invalid'
hover_s = 'hover'

STATE_NAMES = {
    active_s, disabled_s, pressed_s, focus_s, selected_s, background_s, readonly_s, alternate_s,
    invalid_s, hover_s
}

# TODO remove TO_ENUM/NAME?
TO_ENUM: Dict[str, int] = {k: v for k, v in zip(DATA_NAMES, range(0, len(DATA_NAMES)))}
TO_NAME: Dict[int, str] = {v: k for k, v in TO_ENUM.items()}

if __name__ == '__main__':
    print(TO_ENUM)
