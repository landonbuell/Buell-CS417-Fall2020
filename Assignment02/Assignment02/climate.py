"""
Landon Buell
Alejo Hausner
CS417.01 - Assignment02
10 Spet 2020
"""

import sys  # Needed for sys.argv
from typing import List, Dict, Set

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
        for line in in_file.readlines(): 




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

