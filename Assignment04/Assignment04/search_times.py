'''
Read a text file, and determine how often each letter
in the alphabet occurs.
'''
import sys
import bisect
import random
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

    return (0.0, 0)

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

    return (0.0, 0)

def main():
    if len(sys.argv) != 3:
        print ('usage: python',sys.argv[0],'valid_words.txt probe_words.txt')
        sys.exit(1)

    valid_words: List[str] = read_words(sys.argv[1])
    probe_words: List[str] = read_words(sys.argv[2])

    # Here, compute the search times.
    # Use the same probe words, and various subsets
    # of the valid words.

    # For each subset, get the AVERAGE time it takes to search
    # for a probe word, in MICROSECONDS.

if __name__ == '__main__':
    main()

