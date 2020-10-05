"""
Landon Buell
Alejo Hausner
CS 417.01 - Assignment 04
1 October 2020
"""

import sys
import string
from typing import Dict, List

'''
Read a text file, and determine how often each letter
in the alphabet occurs.
'''

class FileProcesser:
    """ Process and Input file for this program """

    def __init__(self,fileLines):
        """ Initialze FileProcesser Instance """
        self.lines = fileLines
        self.InitDictionary()
        self.CleanLines()

    def InitDictionary(self):
        """ Initialize Dictionary Obj """
        self.letterCounterDict = {}                 # dict to hold chars
        for char in string.ascii_lowercase:         # all lower-case letters
            self.letterCounterDict.update({char:0}) # init char w/ 0-cntr
        return self

    def CleanLines (self):
        """ Remove Newline Character from each line of the file """
        newLines = []
        validChars = string.ascii_lowercase     # valid 
        for oldLine in self.lines:              # iterater through each line
            line = oldLine.rstrip("\n\r")       # remove garbage
            line = line.lower()                 # make lowercase 
            newLines.append(line)               # add to new lines
        self.lines = newLines                   # reset attrb       
        return self

    def LetterCounter(self):
        """ Count Letter Occurances in File """
        for line in self.lines:     # iter through each line
            for char in line:       # each char in the string
                if char not in self.letterCounterDict.keys():   # not in dict:
                    continue                                    # skip char
                else:                                           # already in dict
                    self.letterCounterDict[char] += 1           # incr by 1
        return self

    def ComputeLetterFrequencies (self):
        """ Compute Frequency of Each letter in the text File """
        self.totalLetters = 0                           # counter for chars
        self.letterFrequencies = {}                     # hold all frequencies
        for val in self.letterCounterDict.values():     # iter through dict
            self.totalLetters += val                        # add occurance
        for (key,val) in self.letterCounterDict.items():    # get (key,val)
            charFreq = {key:(val/self.totalLetters)}        # compute {Char:freq} pair
            self.letterFrequencies.update(charFreq)     # add to freq dictionary
        return self


def get_frequencies(filename: str) -> None:
    '''
    1. Open a text file.
    2. Read all its lines.
    3.    Turn each line to lower case (use .lower() )
    4.    Ignore any letters that are not a-z (use string.ascii_lower)
    5.    Compute the counts for each letter
    6. Go through all the letters,
    6.    Compute the frequency of each letter.
    7.    Print the letter, and its frequency.

    Parameter:
    ---------
    filename: the name of the text file
    '''
    try:
        file = open(filename, 'r')
        lines: List[str] = file.readlines()
    except UnicodeDecodeError as e:
        file = open(filename, 'r', encoding='utf-8')
        lines: List[str] = file.readlines()

    FileData = FileProcesser(lines)     # create file process inst.
    FileData.LetterCounter()            # count chars 
    FileData.ComputeLetterFrequencies() # compute freqs.

    for (key,val) in FileData.letterFrequencies.items():  # each letter
        print(str(key)+" "+str(val))   # print letter occurance

def main():

    if len(sys.argv) != 2:
        print ('usage: python', sys.argv[0], '<filename>')
        sys.exit(1)
    fileName = sys.argv[1]
   
    #fileName = "A_Wasted_Day.txt"
    get_frequencies(fileName)

if __name__ == '__main__':
    main()

