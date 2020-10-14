'''
Read a text file, and determine how often each letter
in the alphabet occurs.
'''

import sys
import bisect
import random
import time
from typing import List, Tuple

def read_words(filename: str) -> List[str] :
    '''
    Read a file of words, and return its contents as a list
    Don't forget to rstrip('\n\r') each line!
    Don't forget to return the list!

    Parameter:
    ---------
    filename: the name of the file of words

    Returns:
    -------
    The words, in a list.
    '''
    file = open(filename, 'r')
    words = []
    for line in file.readlines():
        words.append(line.rstrip("\n\r"))
    return words

def linsearch_time(probe_words: List[str], valid_subset: List[str])\
    -> Tuple[float, int]:
    """
    1. Get the time,
    2. for each probe word, do "if probe_word in valid_subset"
    3. as you go, count the # of words found
    4. Get the time again.
    5. return the time, and the number of words found.

    Parameters:
    ----------
    probe_words: the probe words
    valid_subset: the valid words

    Returns:
    -------
    a tuple with the time, and the # found
    """
    numFound = 0
    t0 = time.time()                # start time
    for word in probe_words:        # each probe word
        if word in valid_subset:    # in the subset
            numFound += 1           # inc counter by 1
    tf = time.time()                # end time
    dt = tf - t0                    # time difference
    return (dt,numFound)            # (time,words found)

def bsearch_time(probe_words: List[str], valid_subset: List[str])\
    -> Tuple[float, int]:
    """
    This is just like linsearch_time, but do binary search,
    not linear search.
    Parameters:
    ----------
    probe_words: the probe words
    valid_subset: the valid words

    Returns:
    -------
    a tuple with the time, and the # found
    """
    print("BISECT SEARCH TIME NOT IMPLEMENTED")
    raise NotImplementedError()
    valid_subset = sorted(valid_subset) # sort the subset
    numFound = 0
    t0 = time.time()                # start time

    # Bisect search here

    dt = tf - t0                    # time difference
    return (time.time(),numFound)   # (time,words found)


    return (0.0, 0)

def main():

    if len(sys.argv) != 3:
        print ('usage: python',sys.argv[0],'valid_words.txt probe_words.txt')
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # hard-code values for development
    #file1 = "valid_words.txt"
    #file2 = "prob_words.txt"

    valid_words: List[str] = read_words(file1)
    probe_words: List[str] = read_words(file2)

    # Here, compute the search times.
    subsetSizes = [100,200,500,1000,2000,5000,10000,20000,42869]
    # Use the same probe words, and various subsets
    # of the valid words.
    subsetCounts = []
    timeBisect = "BISECT TIME NOT IMPLEMENTED"

    for n in subsetSizes:
        wordSubset = valid_words[:n]    # choose the subset size
        (timeLinear,counts) = linsearch_time(probe_words,wordSubset)
        #(timeBisect,counts) = bsearch_time(probe_words,wordSubset)
        timeLinear *= (1e6 / len(probe_words))       # convert to us, scale by n words
        #timeBisect *= (1e6 / len(probe_words))       # convert to us, scale by n words

        print(n,counts,timeLinear,timeBisect)

    # For each subset, get the AVERAGE time it takes to search
    # for a probe word, in MICROSECONDS.

if __name__ == '__main__':
    main()

