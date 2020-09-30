"""
Landon Buell
Alejo Hausner
CS 417.01 - Assignment 03
22 Sept 2020
"""

import sys
from typing import Dict, List, Tuple

"""
Print some text in large letters, 5x7, on the terminal.
"""


def get_text() -> str:
    '''
    Create and return a single string, using the words in sys.argv
    Method: use " ".join(some list)

    Returns:
    a single string, with all the letters in the command-line arguments
    '''
    text = ""           # text to be outputted
    for arg in sys.argv[1:]:    # each argument (sep by spaces)
        text += arg             # add the word
        text += " "             # add a space
    text = text[:-1]    # remove last space
    return text         # return text string

def get_blocks(filename: str) -> Dict[str, List[str]]:
    """
    Read a file containing 96 5x5 blocks, which are pictures
    for all the characters used in English text:
    punctuation, upper-case and lower-case letters.

    Parameter:
    filename : name of the file containing the blocks

    Returns:
    a dictionary: keys are single letters, values are 5x7 blocks.
    """
    matrices: Dict[str, List[str]] = dict()
    fileHandle = open(filename,mode="r")    # open file
    fileData = fileHandle.readlines()       # get all lines
    for i in range(0,len(fileData),8):      # iterate by line
        textKey = fileData[i].strip("\n\r")     # remove excess
        textVal = []                            # matrix to hold char data
        for j in range (i+1,i+8,1):             # the next 7 lines are the data
            textVal.append(fileData[j].strip("\n\r"))
        newDict = {str(textKey):textVal}
        matrices.update(newDict)
    return matrices

def get_text_height(text: str) -> int:
    """Computes the number of block-rows needed to print some text

    Parameter:
    text : the text to be printed

    Returns:
    The number of rows.  Each block takes up 6 columns, and you can
    fit 13 blocks in a 79-column line.

    text                    height
    "ABC"                   1
    "1234567890"            1   (can fit 10 letters in one row)
    "12345678901"           2   (need another row for 11th letter)
    """
    textList = list(text)       # convert text to list
    shapedList = []             # temp list
    for i in range(0,len(textList),10):     # iterate, inc by 10
        shapedList.append(textList[i:i+10]) # add elements
    return len(shapedList)      # 0-th axis in number of rows

def make_picture(text_height: int) -> List[List[str]]:
    """
    Create and return a 2D list of spaces.  Each space is a pixel.

    Parameter:
    The number of rows of blocks

    Returns:
    A list of lists of strings.  The width is 10*7, and the height is
    text_height * 8.
    """
    picture = []            # "master" list
    for i in range(text_height*8):  # each row
        rowList = []                # init empty list for row
        for j in range(10*7):       # each elem in the row
            rowList.append(" ")     # add an empty string
        picture.append(rowList)     # add to picture
    return picture

def print_picture(picture: List[List[str]]) -> None:
    """
    Assemble each row in the picture (currently each row is a list of str),
    and print them.
    Again, use "".join()

    Parameter:
    A 2D list of strings (the pixels).
    """
    for i in range (len(picture)):  # each row of the picture
        for j in range(len(picture[i])):    # in this particular row
            if picture[i][j] == "_":        # if undersc.
                picture[i][j] = " "         # replace w/ sp.
            
    # Print the array now that "_" -> " "
    for i in range (len(picture)):  # each row of the picture
        outputStr = ""              # init emty str
        for j in range(len(picture[i])):    # in this particular row
            if picture[i][j] == "":             # if empty str
                outputStr += " "
            else:
                outputStr += picture[i][j]      # add str to output
        print(outputStr)
    return None


def put_pixel(x: int, y: int, c: str, picture: List[List[str]]) -> None:
    """Set one pixel in the picture"""
    picture[y][x] = c
    return None

def draw_letter(picture: List[List[str]], letter: str, text_width: int,
                text_row: int, text_col: int,
                blocks: Dict[str, List[str]]) -> Tuple[int,int]:
    """Draw a one-block sprite onto the pixel picture.

    Parameters:
    ----------
    picture: the pixels
    letter: the letter to be drawn as a 5x7 block
    text_width: number of columns that fit on the picture (10)
    text_col: the row where letter goes
    text_col: the column where the letter goes
    blocks: the 5x7 pictures of all the possible letters

    Returns:
    A tuple, with the updated (text_row, text_col), where the NEXT
    letter should go.
    """
    if letter != " ":           # NOT a space
        sprite = blocks[letter]
        spriteWidth,spriteHeight = 5,7
        for x in range(text_col,text_col+spriteWidth):      # each row
            for y in range(text_row,text_row+spriteHeight): # each col
                symbol = sprite[y-text_row][x-text_col]     # get the symbol
                put_pixel(x,y,symbol,picture)               # add the pixels
        if x >= 65:                          # end of line
            return (text_row + 8, 0)        # inc row, reset col
        else:                               # not end of line
            return (text_row,text_col+7)    # inc row by 0, col by 8
    else:                                   # letter is a space
        if text_col >= 68:
            return (text_row + 8, 0)        # inc row, reset col
        else:
            return (text_row,text_col+2)

def main():
    '''
    This function controls the whole process
    '''

    # Get the text from sys.argv
    text: str = get_text()
    #cotext = "Hello World byebye"     # hard-code for development

    # Read the blocks from the matrix file
    blocks: Dict[str, List[str]] = get_blocks('matrix_5x7.txt')

    # Compute #rows and #columns needed for the text
    text_height: int = get_text_height(text)
    text_width: int = 13

    # Create the 2D array of pixels
    picture: List[List[str]] = make_picture(text_height)

    # Initial letter's position
    (text_row, text_col) = (0, 0)
    letter: str
    for letter in text:

        # Draw the letter, and get the next letter's position
        (text_row, text_col) = draw_letter(picture, letter,
                                           text_width,
                                           text_row, text_col,
                                           blocks)

    # Print the picture you just made
    print_picture(picture)

if __name__ == '__main__':
    main()


