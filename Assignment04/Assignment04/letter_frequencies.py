"""
Landon Buell
Alejo Hausner
CS 417.01 - Assignment 04
1 October 2020
"""

import sys
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
        self.RemoveNewLines()

    def RemoveNewLines (self):
        """ Remove Newline Character from each line """
        for line in self.lines:         # iterater through each line
            line = line.replace("\n","")
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

    FileData = FileProcesser(lines)

def main():
    """
    if len(sys.argv) != 2:
        print ('usage: python', sys.argv[0], '<filename>')
        sys.exit(1)
    fileName = sys.argv[1]
    """
    fileName = "A_Wasted_Day.txt"
    get_frequencies(fileName)

if __name__ == '__main__':
    main()

