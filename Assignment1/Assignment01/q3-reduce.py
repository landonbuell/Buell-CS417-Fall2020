"""
Landon Buell
Alejandro Hausner
CS 417.01
31 August 2020
"""

        #### IMPORTS ####

import numpy as np
import sys

        #### CLASS DEFINITIONS ####

class Task03:
    """ Execution Object For Assignment01 - Question 3 """

    def UserInput(self):
        """ Accept and process Command-Line User input """
        while True:
            try:
                numerator = int(input("Enter Numerator: "))
                denominator = int(input("Enter Denominator: "))
                if denominator == 0:
                    raise ValueError("Denomonator cannot be zero!")
                    sys.exit()
                else:
                    break
            except:
                raise ValueError("Inputs must be of type: int")
        return numerator,denominator


    def gcd(self,a,b):
        """ Compute Greatest Common Denominator of a and b """
        while b != 0 :          # while not 0
            a,b = b , a % b     # get remainder
        return a                # gcd

    def Reduce (self,A,B):
        """ Reduce A/B using GCD """
        GCD = self.gcd(A,B)
        A,B = A/GCD , B/GCD     # reduce
        return int(A),int(B)    # return integer equivalent

            #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    Executable = Task03()                       # make instance
    inputA,inputB = Executable.UserInput()      # get user input

    outputA,outputB = Executable.Reduce(inputA,inputB)  
    print("Reduction:",outputA,"/",outputB)
