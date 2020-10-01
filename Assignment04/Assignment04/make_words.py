import sys
from typing import List, Dict

def read_frequencies(filename: str) -> Dict[str, float]:
    '''
    Read a file of frequencies.
    Each line has a letter, a space, and a frequency, like this:

    a 0.0773698678727
    c 0.0239868759422
    b 0.0123259732198
    e 0.128225591913
    ...

    Parameter:
    ---------
    filename: name of the file with frequencies

    Returns:
    -------
    A dictionary: each key is a letter, each value is a frequency.
    '''
    frequencies: Dict[str, float] = dict()
    file = open(filename, 'r')
    line: str
    for line in file.readlines():
        line = line.rstrip('\n\r')
        letter: str
        s_freq: str
        (letter, s_freq) = line.split()
        frequencies[letter] = float(s_freq)
    return frequencies

def make_words(frequencies: Dict[str, float], n_words: int) -> None:
    '''
    Use the frequencies to generate 5-letter random strings which
    might be english words.

    Technique:
    1. Get the cummulative frequencies.  This is a list
       of numbers, from 0.0 to 1.0, derived from the frequencies.
       The first value is the frequency['a']
       The next value is frequency['a']+frequency['b']
       The next value is frequency['a']+frequency['b']+frequency['c']
       and so on.
       (obviously you need a loop)

    2. Make n_words words, using 5 random letters,
       which have English-like frequencies.

    To get a letter that has English-like frequency, do this:
       - generate a random number from 0.0 to 1.0 (use random.random())
       - go through the cummulative frequencies, and find two values
         that bracket your number.
       - get the corresponding letter.

    Parameters:
    -----------
    frequencies : a dictionary of frequencies
    n_words: how many 5-letter words to generate

    Output:
    -------
    prints n_words English-like words.
    '''
    pass

def main():

    if len(sys.argv) != 3:
        print ('usage: python',sys.argv[0],'freqs.txt n_words')
        sys.exit(1)

    frequencies: Dict[str, float] = read_frequencies(sys.argv[1])
    n_words: int = int(sys.argv[2])

    make_words(frequencies, n_words)

if __name__ == '__main__':
    main()

