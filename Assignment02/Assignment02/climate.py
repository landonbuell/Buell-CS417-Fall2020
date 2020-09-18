"""
Landon Buell
Alejo Hausner
CS417.01 - Assignment02
10 Spet 2020
"""

import sys  # Needed for sys.argv
import numpy as np
from typing import List, Dict, Set
import datetime

class Math:

    @staticmethod
    def ArgMax(array):
        """ Return index "i" of maximum value in array """
        max = -np.inf       # max value
        index = 0           # index of 
        for i in range(len(array)):
            if array[i] > max:      # greater than current max?
                max = array[i]      # set new max
                index = i           # store that index
            else:
                pass                # do nothing
        return index

    @staticmethod
    def ArgMin (array):
        """ Return index "i" of minimum value in array """
        min = +np.inf           # max value
        index = 0               # index of 
        for i in range(len(array)):
            if array[i] < min:      # smaller than current max?
                min = array[i]      # set new min
                index = i           # store that index
            else:
                pass                # do nothing
        return index

class ClimateData:

    def __init__(self,in_file,out_file):
        """ Initialize Object Instance """
        self.in_file = in_file
        self.out_file = out_file
        fileHandle = open(self.in_file,mode="r")
        self.fileLines = fileHandle.readlines()
        fileHandle.close()
        self.n_lines = len(self.fileLines)
        self.cleanDATEs = []

        self.outputHeader = ["Day","Avg precip","Avg low","Avg high",
                             "Min low","Max high","Min low year","Max high year"]

    def OrganizeFileLines(self):
        """ Organize All file data, store in self """
        self.DATEs,self.PRCPs,self.TMINs,self.TMAXs = [],[],[],[]
        for i in range(1,self.n_lines):                     # each line, ignoring header
            lineContent = self.fileLines[i].rstrip("\r\n")  # get the string
            fields = lineContent.split(",")                 # split by comma
            if (fields[2] == "") or (fields[3] == ""):  # empty TMIN or TMAX
                continue                                # skip day
            else:                                       # otherwise
                self.TMINs.append(int(fields[2]))       # add to list
                self.TMAXs.append(int(fields[3]))       # add to list
            if (fields[1] == ""):                       # no precip rec.
                self.PRCPs.append(0.0)                  # add 0 units
            else:                                       # otherwise
                self.PRCPs.append(float(fields[1]))     # add measured val
            self.DATEs.append(fields[0])                # add date
        
    def ProcessDates (self):                             
        """ Organize and Correct all Dates in the dates list """
        self.years = []
        for i,date in enumerate(self.DATEs):            # each date obj
            if i == 0:                                  # initial date to process
                if "-" in date:            
                    # Format: YYYY-MM-DD
                    fields = date.split("-")    # Split at dash
                    year,month,day = int(fields[0]),int(fields[1]),int(fields[2])
                elif "/" in date:
                    # Format DD/MM/YYYY
                    fields = date.split("/")    # Split at slash
                    year,month,day = int(fields[2]),int(fields[1]),int(fields[0])
                else:
                    print("\n\tERROR - Unhandled format!")
                    raise ValueError()
            else:           
                if "-" in date:            
                    # Format: YYYY-MM-DD
                    fields = date.split("-")    # Split at dash
                    month,day = int(fields[1]),int(fields[2])
                elif "/" in date:
                    # Format MM/DD/YYYY
                    fields = date.split("/")    # Split at slash
                    month,day = int(fields[0]),int(fields[1])
                else:
                    print("\n\tERROR - Unhandled format!")
                    raise ValueError()
                if (month == 1) & (day == 1):       # new years?
                    year += 1                       # increment years
                    self.years.append(year)
            self.cleanDATEs.append(str(year)+"-"+str(month)+"-"+str(day))           
        return self

    def CreateDictionaries(self):
        """ Add Data by date to dictionaries """
        self.dictPrcp,self.dictTmin,self.dictTmax = {},{},{}
        # Iterate through all data
        for date,prcp,Tmin,Tmax in zip(self.cleanDATEs,self.PRCPs,self.TMINs,self.TMAXs):
            key = self.GetFormattedDate(date)       # get date string
            # Not in the dictionary, make empty list for it
            if key not in self.dictPrcp:           
                self.dictPrcp.update({key:[]})  
                self.dictTmin.update({key:[]})  
                self.dictTmax.update({key:[]})  
            # Always add val to list
            self.dictPrcp[key].append(prcp) 
            self.dictTmin[key].append(Tmin) 
            self.dictTmax[key].append(Tmax) 

        # Lastly, remove leap day
        leapDay = "2-29"
        self.dictPrcp.pop(leapDay)
        self.dictTmin.pop(leapDay)
        self.dictTmax.pop(leapDay)

        return self

    def GetFormattedDate(self,datestring):
        """ return current 'DD/MM' as string """
        fields = datestring.split("-")              # split by dahses
        return str(fields[1])+"-"+str(fields[2])    # feilds new str  

    def ComputeDataForDay(self,dayStr):
        """ Compute Statisitcs for a Single Given Day by key 'DD/MM' """
        avg_precip = sum(self.dictPrcp[dayStr])/len(self.dictPrcp[dayStr])
        avg_high = sum(self.dictTmin[dayStr])/len(self.dictTmin[dayStr])
        avg_low = sum(self.dictTmax[dayStr])/len(self.dictTmax[dayStr])
        min_low = min(self.dictTmin[dayStr])
        max_high = max(self.dictTmax[dayStr])

        # need to implement
        low_idx = Math.ArgMin(self.dictTmin[dayStr])
        high_idx = Math.ArgMax(self.dictTmax[dayStr])
        try:
            low_year = self.years[low_idx]
        except:
            low_year = None
        try:
            high_year = self.years[high_idx]
        except:
            high_year = None

        # Return the row of data
        return [dayStr,avg_precip,avg_low,avg_high,
                min_low,max_high,low_year,high_year]

    def WriteOutputFile(self):
        """ Write Specified Output file to local disk """
        outputFile = open(self.out_file,mode="w")
        outputFile.writelines(str(x)+"," for x in self.outputHeader)
        outputFile.writelines("\n")

        for day in self.dictPrcp.keys():        # iter by day
            statsList = self.ComputeDataForDay(day)
            outputFile.writelines(str(x)+"," for x in statsList)
            outputFile.writelines("\n")

        outputFile.close()
        return self    
            
def get_climate(in_filename: str, out_filename: str) -> None:
    """Read historical weather from in_filename, write climate to out_filename.

    Parameters
    ----------
    in_filename :  name of the input file
    out_filename : name of the output file
    """
    Climate = ClimateData(in_filename,out_filename)
    """
    What you should do:
    1. Read each line of in_file
    2. Skip the first (header) line
    3. Split each line on commas
    4. Get the year, month, and day
    5. Update the statistics (total precip, total low temp, etc)
    6. When done, open the output file.
    7. for each day of the year:
    8. Compute the climate for the day, write to output file.
    """
    Climate.OrganizeFileLines() 
    Climate.ProcessDates()
    Climate.CreateDictionaries()
    
    Climate.WriteOutputFile()

    return None

def usage():
    """Complain that the user ran the program incorrectly."""
    sys.stderr.write('Usage:\n')
    sys.stderr.write('  python climate.py <input-file.csv> <output-file.csv>\n')
    sys.exit()

def main():
    """
    if len(sys.argv) != 3:
        usage()
        sys.exit()
    
    in_filename: str = sys.argv[1]
    out_filename: str = sys.argv[2]
    """

    # Hard-code arguments for debugging purposes
    in_filename = "03824-weather-history.csv"
    #in_filename = "03824-weather-1895-to-1897.csv"
    out_filename = "03824-climate.csv"

    get_climate(in_filename, out_filename)

if __name__ == '__main__':
    main()

