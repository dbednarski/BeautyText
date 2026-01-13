from __future__ import print_function, unicode_literals
import re
import numpy as np
import os.path
import errno


class BeautyText:
    """Class for beauty text printing.

    This class is used to process a crude text and fits in an maximum
    number of characters by line. There is also an option to justify the
    text.

    Attributes:
            text (str): Raw text.
           nchar (int): Number of max characters per line
        justify (bool): Justify the text?
             separator: Type of paragraph separator
    """ 

    verbose = True
    """
        Attribute to show error messages
    """

    def __init__(self, nchar = 40, justify = False, separator="double"):
        self.__text = None
        self.__nchar = nchar
        self.__justify = justify


        if separator not in ("single", "double"):
            raise ValueError("Invalid separator value. It must be 'single' ou 'double'.")

        self.__separator = separator
        
        
    def setParams(self, nchar = None, justify = None, separator = None):
        """Sets/resets *nchar* and/or *justify* attributes.

            Args:
               nchar (int, optional): Number of max characters per line
            justify (bool, optional): Justify the text?
        """ 

        if separator not in ("single", "double"):
            raise ValueError("Invalid separator value. It must be 'single' ou 'double'.")

        if nchar != None:
            self.__nchar = nchar
        if justify != None:
             self.__justify = justify
        if separator != None:
             self.__separator = separator
        
        
    def getParams(self):
        """Returns *nchar* and *justify* attributes.

            Returns:
               :obj:`dictionary`: with the attributes nchar and justify
        """ 
        return {
                "nchar": self.__nchar,
                "justify": self.__justify,
                "separator": self.__separator
               }
        
    
    def readRawText(self, path):
        """Sets *text* attribute by reading the text file *path*.

            Args:
               path (str): The path (including the name) of the text file to be read

            Returns:
                bool: True, in case of success; False, otherwise.

        """ 
        
        # Getting the input text inside the text file as a list whose parameters are paragraphs of the file
        try:
            with open(path,"r+") as f:
                self.__text = [li.replace("\n","") for li in f.readlines()]
        except:
            if self.verbose:
                print("ERROR: \"{}\" is not a text file or is not readable.".format(path))
            return False
            
        return True
        

    def setRawText(self, text):
        """Set *text* attribute by reading a string *text*.

            Params:
               text (str): The string to be assigned as the attribute
        """ 
        
        if text.endswith("\n"):
            text = text[:-1]

        self.__text = text.split("\n")


    def getRawText(self):
        """Return the *text* attribute.

            Returns:
               str: The attribute *text*
        """ 
        return "\n".join(self.__text)


    def getBeautyText(self):
        """Return the formatted *text* attribute.

            Returns:
               str: The formatted attribute *text*
        """ 
        textout = self.__manipulate()
        if textout == False:
            return None
        return textout
        

    def saveBeautyText(self, path):
        """Save the formatted *text* attribute inside the file *path*.

            Args:
               path (str): The path (including the name) of the file to be written.

            Returns:
                bool: True, in case of success; False, otherwise.
        """ 
        textout = self.__manipulate()
        if textout == None:
            return False
        if os.path.isfile(path):
            if self.verbose:
                print("ERROR: file \"{}\" already exists".format(path))
            return False
        try:
            with open(path,"w") as f:
                f.write(textout)
                pass
        except IOError as x:
            if self.verbose:
                if x.errno == errno.EACCES:
                    print("ERROR: no permission to write \"{}\" inside the directory.".format(path))
                elif x.errno == errno.EISDIR:
                    print("ERROR: \"{}\" is a directory.".format(path))
            return False
            
        return True


    def __manipulate(self):
        # This function process the attribute *text* to the format specified by the others
        # attributes *nchar* and *justify*.

        if self.__text == None:
            if self.verbose:
                print("ERROR: no \"text\" parameter/attribute defined.")
            return None

        # `text_out` will stock each paragraph as a list component; each paragraph is a list composed by lines
        text_out = []
        paragraphs = []

        for line in self.__text:

            # In case of new paragraph
            if self.__separator  == "single":
                paragraphs += [""]
            elif self.__separator  == "double" and re.fullmatch(r'[ \t]*', line):
                paragraphs += [""]
                continue

            # If it is the first line
            if len(paragraphs) == 0:
                paragraphs += [line.strip()]
            # If it is a continuation of a paragraph
            else:
                if len(paragraphs[-1]) != 0:
                    paragraphs[-1] += " "
                paragraphs[-1] += line.strip()

        # Loop on the paragraphs
        for i, paragraph in enumerate(paragraphs):

            specialword = ""

            if i != 0:
                if self.__separator == "single":
                    text_out += "\n"
                else:
                    text_out += "\n\n"
            text_out += [""]

            # Loop on the words
            for word in paragraph.split(' '):

                # Case the size of line exceeds the allowed maximum characters,
                # conclude the line processing
                if len(text_out[-1]) + len(word) + len(specialword) > self.__nchar:
                    if self.__justify:
                        justified = self.__justifyLine(text_out[-1][:-1])
                        if justified == False:
                            return None
                        text_out[-1] = justified + "\n"
                    else:
                        text_out[-1] = text_out[-1][:-1] + "\n"
                    text_out += [""]
                    
                if len(word) != 0 and word[-1] == "\\":
                    specialword += word[:-1] + " "
                    continue

                if specialword == "":
                    text_out[-1] += word + " "
                else:
                    text_out[-1] += specialword + word + " "
                    specialword = ""

            # Remove the last dummy space
            text_out[-1] = text_out[-1][:-1]

        return "".join(text_out)


    def __justifyLine(self, line):
        # This function receives a string `line` and returns this string fitted
        # within `nchar` characters. The final `line` length is reached by
        # increasing the spaces between the words.

        
        # `line_arr` will stock each word as a list component
        line_arr = [li + " " for li in line.split(' ')[:-1]] + [line.split(' ')[-1]]
        
        # `left` represents the number of spaces to be included in the `line`
        left = self.__nchar - len(line) + 1
        nspaces = len(line_arr) - 1
        
        if nspaces == 0:
            if self.verbose:
                print("ERROR: impossible justify the text. Try a larger \"nchar\" parameter/attribute value.")
            return False
        
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
        
