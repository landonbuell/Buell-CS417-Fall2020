"""
Landon Buell
Alejo Hausner
Lab 01
2 Sept 2020
"""

def sort_three(a, b, c):
    """ Sort three Numbers in Acsending Order """
    if (a < b):
        if (b < c):
            print(a,b,c)
        else:
            if (a < c):
                print(a,c,b)
            else:
                print(c,a,b)
    else: # must have b < a
        if (a < c):
            print(b,a,c)
        else:
            if (b < c):
                print(b,c,a)
            else:
                print(c,b,a)

    return None


def delete_at(alist, k):
    """ return a list, given a delted item """
    outputList = alist[:k] + alist[k+1:]
    return outputList


def insert_at(alist, i, x):
    """ Return list with an element inserted """
    outputList = alist[:i] + [x] + alist[i:]
    return outputList


def max_difference(list1, list2):
    """ Return biggest difference from numbers on two lists """
    biggestDiff = 0         # initialize
    for i in list1:         # first list
        for j in list2:     # second list
            diff = abs(i - j)
            if diff > biggestDiff:
                biggestDiff = diff
    return biggestDiff      # return difference

'''
Main program to test the above functions.
Don't change this code.
'''
def main():
    sort_three(1,2,3)
    sort_three(1,3,2)
    sort_three(2,1,3)
    sort_three(2,3,1)
    sort_three(3,2,1)
    sort_three(3,1,2)
    print()

    print (delete_at(['one', 'two', 'three', 'four'], 0))
    print (delete_at(['one', 'two', 'three', 'four'], 1))
    print (delete_at(['one', 'two', 'three', 'four'], 2))
    print (delete_at(['one', 'two', 'three', 'four'], 3))
    print ()

    print (insert_at(['one', 'two', 'three'], 0, 'and'))
    print (insert_at(['one', 'two', 'three'], 1, 'and'))
    print (insert_at(['one', 'two', 'three'], 2, 'and'))
    print (insert_at(['one', 'two', 'three'], 3, 'and'))
    print ()

    print (max_difference([1, 2, 3], [4, 5, 6]))
    print (max_difference([-6, -5, -4], [-3, -2, -1]))


'''
Call main() when the module is run
'''
if __name__ == '__main__':
    main()

