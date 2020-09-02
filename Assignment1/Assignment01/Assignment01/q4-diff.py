"""
Landon Buell
Alejandro Hausner
CS 417.01
31 August 2020
"""

        #### IMPORTS ####

import numpy as np
import os
import sys

        #### CLASS DEFINITIONS ####

class Task04:
    """ Execution Object For Assignment01 - Question 4 """

    def __init__(self,file1,file2):
        """ Initialize Class Objects Instance """
        self.files = [file1,file2]
        self.fileContents = []
        
    def FilesExists(self):
        """ Test if List of Files does not exist """
        for file in self.files:                 # each file
            if os.path.isfile(file) == False:   # make sure it exists
                raise FileNotFoundError()       # raise error
                sys.exit(1)                     # exit
        return self                             # return instance

    def ReadFiles(self):
        """ Read each file from either file """
        for fileToRead in self.files:
            fileObject = open(fileToRead,mode="r")      # file object
            fileContents = fileObject.readlines()       # store lines in list
            fileObject.close()
            for line in fileContents:       # each line
                line.rstrip("\n")
            self.fileContents.append(fileContents)    # add to self
        return self

    def SameContents(self):
        """ Test of 2 files have the same Content """
        for lineA,lineB in zip(self.fileContents[0],self.fileContents[1]):
            # Iterate through both files
            if lineA == lineB:      # lines are the same
                continue            # keep going 
            else:                   # not the same
                return False        # break, files are diff
        return True                 # files are the same

        #### MAIN EXECUTABLE ####
        
if __name__ == '__main__':

    # Accept Command Line Input
    if len(sys.argv) != 3:
        print('Usage:\n  python diff.py <file1> <file2>')
        sys.exit(1)

    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]

    # Execution
    Executable = Task04(fileName1,fileName2)
    Executable.FilesExists()            # tests if files exist!
    Executable.ReadFiles()              # read files

    if (Executable.SameContents() == True):     # test if lines match
        print("Files",fileName1,"and",fileName2,"are the same!")
    else:
        print("Files",fileName1,"and",fileName2,"are not the same!")

    

