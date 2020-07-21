import sys
from typing import List
from objects.buildObject import BuildObject
from parsers.mainParse import startParse
from output.output import outputBuild
from forgeExceptions import ForgeException


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # TODO finalize usage
        #   define options

        #   No listing file option
        #   Print available ttk themes
        #   compile using specific theme?
        #       removes need to specify the theme in forge file

        print("Usage:\n"
              "\tforge inFile")


def forge(inputFiles: List[str], *, options):
    # TODO Output file names and locations
    #   Add to listing file?

    bo = BuildObject()

    try:
        for x in inputFiles:
            startParse(bo, x)

        bo.checkClaims()
        # TODO build output func call params
        outputBuild(bo)
    except ForgeException as e:
        print(e.message)

    exit(0)

# TODO
#   2) Code parsers for each
#   3) Code output functionality
