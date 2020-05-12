from build.buildConsts import TO_NAME


class ForgeException(Exception):
    def __init__(self):
        super().__init__()
        self.message = ''


class ParseException(ForgeException):
    def __init__(self, line, idx, message):
        self.message = f'{message}, line: {idx}: "{line}"'


class InvalidParamException(ForgeException):
    def __init__(self, objName: str, paramName: str):
        super().__init__()
        self.message: str = f'Object "{objName}": Invalid parameter "{paramName}"'


class InvalidTypeException(ForgeException):
    def __init__(self, objName: str, paramName: str, validType: int, curType: int):
        super().__init__()
        self.message = f'Object "{objName}": Parameter "{paramName}": ' \
                       f'Invalid type: Expected{TO_NAME[validType]}, got {TO_NAME[curType]}'


class ReDefinitionException(ForgeException):
    def __init__(self, objName: str):
        super().__init__()
        self.message = f'Object "{objName}" has been defined twice'


class ReStyleException(ForgeException):
    def __init__(self, objName: str):
        super().__init__()
        self.message = f'Style "{objName}" has been defined twice'


class ClaimException(ForgeException):
    def __init__(self, objName: str, curParent: str, invalidParent: str):
        super().__init__()
        self.message = f'Object "{objName}" already loaded into "{curParent}", invalid load into "{invalidParent}"'


class DevException(ForgeException):
    def __init__(self, message):
        self.message = f'DEV ERROR: {message}'
