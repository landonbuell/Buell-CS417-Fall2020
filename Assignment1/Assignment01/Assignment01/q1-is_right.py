"""
Landon Buell
Alejandro Hausner
CS 417.01
31 August 2020
"""

        #### IMPORTS ####

import numpy as np

        #### CLASS DEFINITIONS ####

class Assignment1:
    """ Accept and Process Command-Line User Input """

    def __init__(self):
        """ Initialize Class Instance """
        self.sideLabels = ["A: ","B: ","C: "]       # label for each side
        self.inputString = "Enter Length of side "  # string for user input
        self.dx = 1e-10                             # tolerance factor for FP numbers

    def UserInput (self):
        """ Accept & Evaluate User Input for Assignment """
        inputSides = np.array([])           # array to hold side lengths
        for side in self.sideLabels:        # A,B,C
            while True:                     # loop, incase   
                try:
                    userInput = float(input(self.inputString+side))  
                    if userInput <= 0:  # must be > 0
                        print("\n\tERROR! - Side length must be > 0")
                    else:
                        inputSides = np.append(inputSides,userInput)
                        break
                except:
                    print("\n\tERROR! - Input must be type: Float")
        return inputSides

    def IsRightTriangle (self,sideLengths):
        """ Test if 3 side legnths can form a right trangle """
        assert len(sideLengths == 3)    # make sure it IS a triangle
        rightTriangle = False           # set condition to False
        sideSquared = sideLengths**2    # element-wise ^2
        legs = sideSquared[0] + sideSquared[1]
        hypo = sideSquared[2]
        if (legs / hypo) == 1:          # test w/ pythag thm.
            rightTriangle = True        # set to true
        return rightTriangle            # return "Is Right" T/F

        #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    Executable = Assignment1()              # create Executable obj
    sideLengths = Executable.UserInput()    # Get side lengths from user

    for i in range (0,3,1):     # iterate over 3 sides
        # Test A,B,C as Side Lengths
        isRightTriangle = Executable.IsRightTriangle(sideLengths)
        if isRightTriangle == True:     # if right
            break                       # exit loop early
        else:                           # otherwise, roll axis
            sideLengths = np.roll(sideLengths,shift=+1)

    # message to user
    print("Triangle w/ Sides:",sideLengths,"is a right triangle:",isRightTriangle)


