"""
Landon Buell
Alejandro Hausner
CS 417.01
31 August 2020
"""

        #### IMPORTS ####

import numpy as np

        #### CLASS DEFINITIONS ####

class Task02:
    """ Execution Object For Assignment01 - Question 2 """

    def UserInput(self):
        """ Accept and Process User Input at the Command Line """
        while True:
            try:
                n = int(input('Number terms in series? '))
                if n < 1:
                    raise ValueError("n_terms must be integer >= 1")
                else:
                    break
            except:
                raise ValueError("n_terms must be integer")
        return n

    def LeibnitzFormula(self,n_terms):
        """ Compute first n_terms of Leibnitz' Approx of PI """
        approximation = 0           # initialize Approximation
        for i in range (0,n_terms):
            newTerm = (-1)**i / (2*i + 1)
            approximation += newTerm
        approximation *= 4                      # multiply by 4
        return approximation                    # return the approximation

                

        #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    Executable = Task02()       # create exectuabe
    n_terms = Executable.UserInput()                # get user input
    piApprox = Executable.LeibnitzFormula(n_terms)  # find approximation
    print("Liebnitz's appoximation of pi to",n_terms,"terms is:",piApprox)
