import sys
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

    # TODO Output file names and locations
    #   Add to listing file?

    try:
        outputBuild(startParse(sys.argv[1]))
    except ForgeException as e:
        print(e.message)

    exit(0)

# TODO
#   1) Make all parseObjects
#   2) Code parsers for each
#   3) Code output functionality

