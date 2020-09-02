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
   
    def __init__(self,filename):
        """ Initialize Class Object Instance """
        self.filename = filename

    def ReadFile (self):
        """ Read File from local Directory """
        Frame = pd.read_csv(self.filename,delimiter=',',header=None)
        self.classNames = Frame[0]
        self.userNames = Frame[1]
        self.userScores = Frame[2]
        return self

    def StudentScores (self):
        """ Compute Scores for Each student """
        self.scoreDictionary = {}         # dictionary to hold students' scores
        for user in self.userNames:         # each user
            if user not in self.scoreDictionary.keys():   # not in dict
                self.scoreDictionary.update({user:[]})    # update
        for user,score in zip(self.userNames,self.userScores):  # user,score
            self.scoreDictionary[user].append(score)      # add score to user key
        return self

    def StudentAverages (self):
        """ Compute Average score for each student """
        self.meansDictionary = {}                   # dictionary for average scores
        for user in self.scoreDictionary.keys():    # iterate by user
            newValue = {user:np.mean(self.scoreDictionary[user])}   # uers: average
            self.meansDictionary.update(newValue)   # add new score
        return self

    def StudentGPAs (self):
        """ Compute GPA by each student Score """
        self.GPAsDictionary = {}
        for (user,score) in self.meansDictionary.items():    # each user         
            
            if score >= 94:
                newValue = {user:4.0}
            elif score >= 90:
                newValue = {user:3.7}
            elif score >= 87:
                newValue = {user:3.0}
            elif score >= 80:
                newValue = {user:2.7}
            elif score >= 77:
                newValue = {user:2.3}
            elif score >= 74:
                newValue = {user:2.0}
            elif score >= 70:
                newValue = {user:1.7}
            elif score >= 67:
                newValue = {user:1.3}
            elif score >= 64:
                newValue = {user:1.0}
            elif score >= 60:
                newValue = {user:0.7}
            else:
                newValue = {user:0}

            self.GPAsDictionary.update(newValue)
        return self
           
    def PrintResults (self):
        """ Print Results in Tabular format """
        self.userNames = np.unique(self.userNames)  # only unque values
        self.dataDictionary = {"Student":self.userNames,
                              "Average":[x for x in self.meansDictionary.values()],
                              "GPA":[x for x in self.GPAsDictionary.values()]}
        self.Frame = pd.DataFrame(data=self.dataDictionary)
        print(self.Frame)
        return self

        #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    # Get filename from Command Line
    fileName = sys.argv[1]              # get CL args
    #fileName = 'scores.csv'
    Executable = Task05(fileName)       # create executbale instance
    Executable.ReadFile()               # read file contents
    Executable.StudentScores()          # get student by score
    Executable.StudentAverages()        # get student by average
    Executable.StudentGPAs()            # get student by GPS
    Executable.PrintResults()           # assemble & print results

    print("=)")
