#!/usr/bin/env python
#

import argparse, sys
import numpy as np
import os.path



def main(args):
    
    # Getting the input text inside the text file as a list whose parameters are paragraphs of the file
    try:
        with open(args["file"],"r+") as f:
            text_in = [li.replace("\n","") for li in f.readlines()]
    except:
        print("ERROR: \"{}\" is not a text file or is not readable.".format(args["file"]))
        sys.exit(1)

    # `text_out` will stock each paragraph as a list component; each paragraph is a list composed by lines
    text_out = []

    # Getting the others parameters
    nchar = args["num_char"]
    justify = args["justify"]


    # Loop on the paragraphs
    for paragraph in text_in:

        text_out += [""]
        specialword = ""
        # In case of new paragraph
        if paragraph == "" or (len(paragraph) > 0 and paragraph[0] == " "):
            text_out[-1] = "\n\n"
            continue

        # Loop on the words
        for word in paragraph.split(' '):

            # Case the size of line exceeds the allowed maximum characters,
            # conclude the line processing
            if len(text_out[-1]) + len(word) + len(specialword) > nchar:
                if justify:
                    text_out[-1] = justifyLine(text_out[-1][:-1], nchar+1) + "\n"
                else:
                    text_out[-1] = text_out[-1][:-1] + "\n"
                text_out += [""]
                
            if word[-1] == "\\":
                specialword += word[:-1] + " "
                continue

            if specialword == "":
                text_out[-1] += word + " "
            else:
                text_out[-1] += specialword + word + " "
                specialword = ""

        # Remove the last dummy space
        text_out[-1] = text_out[-1][:-1]

#    if justifylast:
#        text_out[-1] = justifyLine(text_out[-1][:-1], nchar-1)

    print "".join(text_out)
    sys.exit(0)



def justifyLine(line, nchar):
    """
    This function receives a string `line` and returns this string fitted
    within `nchar` characters. The final `line` lenght is reached by
    increasing the spaces between the words.
    """
    
    # `line_arr` will stock each word as a list component
    line_arr = [li + " " for li in line.split(' ')[:-1]] + [line.split(' ')[-1]]
    
    # `left` represents the number of spaces to be included in the `line`
    left = nchar - len(line)
    nspaces = len(line_arr) - 1
    
    if nspaces == 0:
        print("ERROR: impossible justify the text. Try a larger \"num_char\" parameter value.")
        sys.exit(1)        
    
    while left > 0:
        # Add one more space in every position where there is already at least one space...
        if left >= nspaces:
            line_arr = [li + " " for li in line_arr[:-1]] + [line_arr[-1]]
            left -= nspaces
        # ...or distribute the `left` number of remaining spaces approximately equal over `line`.
        else:
            for n in map(lambda pos: int(pos), np.linspace(0, nspaces-1, left)):
                line_arr[n] += " "
            break

    return "".join(line_arr)
    
    
    
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
    parser.add_argument("-n", "--num_char", help="Number of max characters in each line (Default = 40)", type=int, default=40)

    args = parser.parse_args()

    return args



if __name__ == "__main__":

    args = parseArguments()

    # Verify if the file with the texto exists and is readable.
    f = args.__dict__["file"]
    if not os.path.isfile(f):
        print("ERROR: file \"{}\" does not exist".format(f))
        sys.exit(1)
    if not os.access(f, os.R_OK):
        print("ERROR: permission denied to read the file \"{}\"".format(f))
        sys.exit(1)

    main(args.__dict__)

#   main()
#    print("You are running the script with arguments: ")
#    for a in args.__dict__:
#        print(str(a) + ": " + str(args.__dict__[a]))
#        print(a)
