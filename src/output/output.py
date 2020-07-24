# File output
from objects.buildObject import BuildObject


# TODO standard dialog function
#   Create alias functions for default dialogs
#       Created by default


def outputBuild(build: BuildObject, mainFile: str, accessFile: str, listingFile: str) -> None:

    with open(mainFile, mode='w') as f:
        # TODO output intro
        #   define master containing class?

        intro = f'import tkinter as tk\n' \
                f'class ForgeGUI:\n' \
                f'    def __init__(self):\n'

        tabs: str = '\t\t'

        f.write(intro)

        lines: str = ''
        for x in build.defined.values():
            lines += tabs + x.outputInit() + '\n'

        f.write(lines + '\n')

        lines = ''

        for x in build.defined.values():
            lines += tabs + x.outputConfig() + '\n'

        f.write(lines + '\n')

        lines = ''

        for x in build.defined.values():
            lines += tabs + x.outputPost() + '\n'

        f.write(lines + '\n')

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