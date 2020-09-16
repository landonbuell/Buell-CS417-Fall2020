"""
Landon Buell
Alejo Hausner
CS417.01 - Assignment02
10 Spet 2020
"""

import sys  # Needed for sys.argv
from typing import List, Dict, Set
import datetime

class ClimateData:

    def __init__(self,in_file,out_file):
        """ Initialize Object Instance """
        self.in_file = in_file
        fileHandle = open(self.in_file,mode="r")
        self.fileLines = fileHandle.readlines()
        fileHandle.close()
        self.n_lines = len(self.fileLines)

        self.outputHeader = ["Day","Avg precip","Avg low","Avg high",
                             "Min low","Max high","Min low year","Max high year"]

    def ProcessInitialDate (self,datestring):
        """ Process a date string """
        if "-" in datestring:
            # format is YYYY-MM-DD
            data = datestring.split("-")
            self.century = int(data[0][:2])
            self.decade = int(data[0][2:])
            self.month = int(data[1])
            self.day = int(data[2])
        elif "/" in datestring:
            # format is DD/MM/YYYY
            data = datesting.split("/")
            self.century = int(data[2][:2])
            self.decade = int(data[2][2:])
            self.month = int(data[1])
            self.day = int(data[0])
        else:
            print("\n\tERROR-Invalid Format for 1st entry")
        return self

    def GetFormattedDate(self):
        """ return current 'MM/DD' as string """
        return str(self.month)+"/"+str(self.day)
            

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
    # 1. Read each line of in_file       
    for i in range(1,Climate.n_lines):     # each line, ignoring header
        lineContent = Climate.fileLines[i].rstrip("\r\n")   # get the string
        fields = lineContent.split(",")                     # split by comma

        if i == 1:          # 1st iter
            Climate.ProcessInitialDate(fields[0])

        print("=)")
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
    in_filename = "03824-weather-1895-to-1897.csv"
    out_filename = "03824-climate.csv"

    get_climate(in_filename, out_filename)

if __name__ == '__main__':
    main()

