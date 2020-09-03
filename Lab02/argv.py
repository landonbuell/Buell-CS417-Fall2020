"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab02
3 Sept 2020
"""

import sys

def print_block(width, height, symbol):
    """ Print 'symbol' as width by height matrix """
    for i in range (height):            # each height unit
        symbolLine = ""                 # each row
        for j in range (width):         # each n cols
            symbolLine += str(symbol)   # add the symbol
        print(symbolLine)
    return None
    
def print_args():
    """ Print User Supplied Command Line Aruguments """
    for arg in sys.argv[1:]:    # all args (except 0-th)
        print(arg)              # print the value
    return None

def print_names():
    """ Print User Supplied Command Line Aruguments """
    print ("Flags:")
    for arg in sys.argv[1:]:        # each arg (except 0-th)
        if arg.startswith("-"):     # leading dash
            print("\t",arg[1:])     # remove dash
    return None

def parse_arguments():
    """ Parse user supplied CommandLine Arguments """
    height,width,symbol = 2,3,"X"   # set defaults
    i = 1                           # init counter
    while (i < len(sys.argv)):      # each arg (except 0-th)
        if sys.argv[i] == '-width':     # width param
            width = int(sys.argv[i+1])  # width is next arg
            i += 2
        elif sys.argv[i] == '-height':  # width param
            height = int(sys.argv[i+1]) # width is next arg
            i += 2
        else:                           # otherwise
            symbol = sys.argv[i]        # this is thr symbol to use
            i +=1
    return (width, height, symbol)

def main():
    print ('-----print_args----------------')
    print_args()

    print ('-----print_names--------')
    print_names()

    print ('-----parse_arguments-----------')
    (width, height, symbol) = parse_arguments()
    print_block(width, height, symbol)

if __name__ == '__main__':
    main()

