# File output
from objects.buildObject import BuildObject
from typing import List


# TODO standard dialog function
#   Create alias functions for default dialogs
#       Created by default


def outputBuild(build: BuildObject, mainFile: str, accessFile: str, listingFile: str) -> None:

    with open(mainFile, mode='w') as f:
        tabs: str = ''

        # TODO output intro
        #   define master containing class?


        lines: List[str] = []
        for x in build.defined.values():
            lines += tabs + x.outputInit() + '\n'


        # TODO output init

        lines = []

        for x in build.defined.values():
            lines += tabs + x.outputConfig() + '\n'

        # TODO output config

        lines = []

        for x in build.defined.values():
            lines += tabs + x.outputPost() + '\n'

        # TODO output post

        # TODO output end

    with open(accessFile, mode='w') as f:
        # TODO access intro
        #   import mainFile

        for x in build.defined.values():
            # TODO output access
            # x.outputAccess()
            pass

    with open(listingFile, mode='w') as f:
        # TODO output listing
        pass