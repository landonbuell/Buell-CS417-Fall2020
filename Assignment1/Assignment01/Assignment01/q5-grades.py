"""
Landon Buell
Alejandro Hausner
CS 417.01
31 August 2020
"""

        #### IMPORTS ####

import numpy as np
import sys
import pandas as pd

        #### CLASS DEFINITIONS ####

class Task05:
   
    def __init__(self,fiename):
        """ Initialize Class Object Instance """
        self.filename = filename

    def ReadFile (self):
        """ Read File from local Directory """
        self.Frame = pd.read_csv(self.filename,delimiter=',')
        print(self.Frame.columns)
        


        #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    # Get filename from Command Line
    fileName = sys.argv[1]              # get CL args
    Executable = Task05(fileName)       # create executbale instance

