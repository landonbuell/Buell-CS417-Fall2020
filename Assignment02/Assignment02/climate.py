"""
Landon Buell
Alejo Hausner
CS417.01 - Assignment02
10 Spet 2020
"""

import sys  # Needed for sys.argv
from typing import List, Dict, Set
import datetime

def ProcessDateString (datestring,currentCentury):
    """ Extract year, month day from string """
    if "-" in datestring:       # slashes:
        # format = YYYY-MM-DD
        splitVals = datestring.split("-")   # split by "-"
        # return datetime obj instance
        return datetime.datetime(year=int(splitVals[0]),
                                 month=int(splitVals[1]),
                                 day=int(splitVals[2]))
    elif "/" in datestring:
        # format = DD/MM/YYY
        splitVals = datestring.split("-")   # split by "-"
        # return datetime obj instance
        return datetime.datetime(year=int(splitVals[2]),
                                 month=int(splitVals[1]),
                                 day=int(splitVals[0]))
    else:
        print("\n\tEROR! - unimplemented format to handle")
        return None



def get_climate(in_filename: str, out_filename: str) -> None:
    """Read historical weather from in_filename, write climate to out_filename.

    Parameters
    ----------
    in_filename :  name of the input file
    out_filename : name of the output file
    """
    in_file = open(in_filename, 'r')

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
    # Read each line of infile
    while True:
        line = in_file.readlines()
        if len(line) == 0:      # last line
            break               # leave loop
        fields = line.split(",")    # split by comma
        # if any feild is an empty string, skip it
        if field in [x for x in feilds] == "":
            continue

        # isolate each feild w/ variable
        date = fields[0]        
        dateTimeObject = ProcessDateString(date)
        precip = fields[1]
        tempMax = fields[2]
        tempMin = fields[3]
                      
        # 







def usage():
    """Complain that the user ran the program incorrectly."""
    sys.stderr.write('Usage:\n')
    sys.stderr.write('  python climate.py <input-file.csv> <output-file.csv>\n')
    sys.exit()

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit()

    in_filename: str = sys.argv[1]
    out_filename: str = sys.argv[2]

    get_climate(in_filename, out_filename)

if __name__ == '__main__':
    main()

