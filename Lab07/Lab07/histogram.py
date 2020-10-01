"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab07
1 October 2020
"""

import sys
from typing import List

def print_histogram(filename: str,
                    n_bins: int) -> None:
    """
    Compute how many numbers fall into each bin.

    Parameters:
    ----------
    filename: text file containing all the numbers
    n_bins: number of bins
    """
    # First, get all the numbers from the data file.

    file = open(filename, 'r')
    lines = file.readlines()

    # This is a 'list comprehension'.  We will talk about them soon.
    numbers = [float(x)
               for line in lines
               for x in line.rstrip('\n\r').split()]
    file.close()

    # Then, use min(numbers) and max(numbers), to get the upper and lower
    # range of the data.

    lo: float = min(numbers)
    hi: float = max(numbers)

    span: float = (hi - lo) * 1.0001

    # Create a list of n_bins counters, initially all zero

    counts: List[int] = [0 for i in range(n_bins)]

    # Then, visit each number,
    #  identify its bin, and
    #  increment that bin's counter.
    #
    # The formula for a bin is:
    #    bin = int((x - lo) / span * n_bins)
    #

    for x in numbers:
        bin = int((x - lo) / span * n_bins)
        counts[bin] += 1

    # Finally, print all the counts, one per line.
    for bin in counts:
        print(bin)

def main():

    if len(sys.argv) != 3:
        print('Usage: python histogram.py <filename> <#bins>')
        sys.exit(1)

    # Get the file name, and # bins
    filename: str = sys.argv[1]
    n_bins: int = int(sys.argv[2])

    # Hardcore Parameters for Development
    #filename: str = "numbers.txt"
    #n_bins: int = 10

    print_histogram(filename, n_bins)

if __name__ == '__main__':
    main()


