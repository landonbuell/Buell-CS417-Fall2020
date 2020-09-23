"""
Landon Buell
Alejo Hausner
CS 417.01
22 Sept 2020
"""

import sys

def print_file(filename):
    """ Print Contents of a given file """
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    print(lines)
    return None

def print_lines(filename):
    """ Print Contents of a given file """
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        print(line.rstrip("\r\n"))
    return None

def print_splits(filename):
    """ Print Contents of a given file """
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        words_in_line = line.split()
        print(words_in_line)
    return None

def print_words(filename):
    """ Print Contents of a given file """
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        words_in_line = line.split()
        for word in words_in_line:
            print(word,end=" ")
    print()
    return None

def words_length(filename):
    """ Print Contents of a given file """
    line_length = 0
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        words_in_line = line.split()
        for word in words_in_line:
            print(word,end=" ")
            line_length += len(word) + 1
    print("Line Length:",line_length)
    return None

def print_reflowed(filename, width):
    """ Print Contents of a given file """
    line_length = 0
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        words_in_line = line.split()
        for word in words_in_line:
            if line_length + 1 + len(word) > width:
                print()
                line_length = 0
            print(word,end=" ")
            line_length += len(word) + 1
    print("Line Length:",line_length)
    return None

def print_right_aligned(filename, width):
    """ Print Contents of a given file Right Justified """
    line_length = 0
    words_list = []
    handle = open(filename,mode="r")
    lines = handle.readlines()
    handle.close()
    for line in lines:
        words_in_line = line.split()       
        for word in words_in_line:        
            if line_length + 1 + len(word) > width:
                print(" "*int(width - line_length),end=" ")
                line_length = 0
                for w in words_list:
                    print(w,end=" ")
                print()
                words_list = []
            words_list.append(word)
            line_length += len(word) + 1
    print(" "*int(width - line_length),end=" ")
    for w in words_list:
        print(w,end=" ")
    print()
    return None

def print_justified(filename, width):
    # Remove the next line!
    print ('print_justified NOT IMPLEMENTED')

def main():
    filename = 'independence.txt'
    width = 40
    print("print file:")
    print("--------------------")
    print_file(filename)
    print("print lines:")
    print("--------------------")
    print_lines(filename)
    print("print splits:")
    print("--------------------")
    print_splits(filename)
    print("print words:")
    print("--------------------")
    print_words(filename)
    print("words length:")
    print("--------------------")
    words_length(filename)
    print("print reflowed:")
    print("--------------------")
    print_reflowed(filename, width)
    print("print right_aligned:")
    print("--------------------")
    print_right_aligned(filename, width)
    print("print justified:")
    print("--------------------")
    print_justified(filename, width)

if __name__ == '__main__':
    main()
