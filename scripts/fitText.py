#!/usr/bin/env python
#

from __future__ import print_function, unicode_literals
import argparse, sys
from beautytext.BeautyText import BeautyText


def main(args):
    
    BeautyText.verbose = True
    text_obj = BeautyText(nchar = args["nchar"], justify = args["justify"])
    if not text_obj.readRawText(args["file"]):
        sys.exit(0)
        
    text_out = text_obj.getBeautyText()
    if text_out != None:
        print(text_out)

    sys.exit(1)


    
def parseArguments():
    """
    This funcion sets the allowed command line input parameters
    and its formats, returning these arguments.

    Some errors can be returned by the builtin functions from
    argparse module.
    """

    # Desciption for the help parameter (-h | --help)
    parser = argparse.ArgumentParser(description="Program to edit the text from \"file\" text file, fitting its content into lines with a maximum length. The output is the modified text printed on the terminal.")

    # Required argument
    parser.add_argument("file", help="Text file with the plain text to be edited.", type=str)

    # Optional arguments
    parser.add_argument("-j", "--justify", help="Justify the text", action="store_true")
    parser.add_argument("-n", "--nchar", help="Number of max characters in each line (Default = 40)", type=int, default=40)

    args = parser.parse_args()

    return args



if __name__ == "__main__":

    args = parseArguments()
    main(args.__dict__)
