# ALL OF THESE FUNCTIONS MUST BE RECURSIVE!
# NO for-loops or while-loops are allowed.

def is_palindrome(s):
    '''
    Return True if the string s is the same when reversed, False if not.
       You MAY NOT use the reversed() function!
    '''
    # Base case: if the length of s is less than 2, it's
    # a palindrome, by default
    if len(s) < 2:
        return True


    # Do some work:
    # If the first and last letters of s are NOT the same,
    # s isn't palindromic; return False
    elif (s[0] != s[-1]):
        return False

    # Otherwise, check if the CORE of s is palindromic:
    # Call is_palindrome, passing it s[1:-1], and return
    else:
        return is_palindrome(s[1:-1])

    # the result of the call.


def count_odds(alist):
    '''
    Return how many numbers in alist are odd.
    '''
    # Base case:
    # If the list is empty, return 0
    if len(alist) == 0:
        return 0

    # Do some work:
    # 1. Call count_odds, and pass it the tail of the list : alist[1:]
    #    It will return the odd count in the tail.  Save that count.
    else:
        odds = count_odds(alist[1:])
    # 2. Check if the first value is odd.
    #    Return the saved count, or the saved count + 1
    if alist[0] % 2 == 0:   # if event
        return odds
    else:                   # if odd
        return odds + 1
    
def max_value(alist):
    '''
    Return the biggest value in alist.
    ASSUMPTION: the list is NOT empty.
    
    You MAY NOT use the max() function!
    '''
    # Base case:
    # If alist has length 1, its max value is the first (and only) element
    if len(alist) == 1:
        return alist[0]

    # Do some work:
    # 1. call max_value, and pass it the tail of the list.
    #    Save the returned value into max_tail.
    else:
        max_tail = max_value(alist[1:])
    # 2. Compare the head value to the max_tail.  Return the bigger
    #    of these two.
        if alist[0] > max_tail:
            return alist[0]
        else:
            return max_tail


def last_index(alist, value):
    '''
    Return the index where value occurs LAST.
    If value does not occur, return -1
    You MAY NOT use rfind()!
    '''
    # Base case:
    # If the list is empty, value can't occur.  Return -1
    if len(alist) == 0:
        return -1
    # Do some work:
    # If the last entry (i.e. alist[-1]) equals value, return that len(alist)-1
    if alist[-1] == value:
        return len(alist)-1
    # Otherwise, call last_index, and pass it a slice of alist without
    # the tail entry.
    else: 
        return last_index(alist[:-1],value)
    # Return the result of that call.


def is_sorted(alist):
    '''
    Return True if all the values in alist
    are in increasing order, False if some value is out of order.
    (Bonus 10%)
    '''
    # Base case:
    # if there are 0 or 1 values, it is sorted (by default).  Return True
    if len(alist) <= 1:
        return True

    # Recursive case:
    # check that first two values are in increasing order, and that
    # the tail is sorted.
    else:
        if alist[0] < alist[1]:
            return is_sorted(alist[2:])
        else:
            return False


def main():
    print( '"abracadabra" is palindromic?', is_palindrome("abracadabra") )
    print( '"abba" is palindromic?       ', is_palindrome("abba") )
    print( '"madam" is palindromic?      ', is_palindrome("madam") )
    print( '"X" is palindromic?          ', is_palindrome("X") )
    print( 'empty string is palindromic? ', is_palindrome("") )
    
    print( '# odd numbers in [1,2,3,4,5]:', count_odds([1,2,3,4,5]) )
    print( '# odd numbers in [2,4,6,8]:  ', count_odds([2,4,6,8]) )
    print( '# odd numbers in []:         ', count_odds([]) )
    
    print( 'max([1,2,3,4]):              ', max_value([1,2,3,4]) )
    print( 'max([4,3,2,1]):              ', max_value([4,3,2,1]) )
    print( 'max([4]):                    ', max_value([4]) )

    print( '4 last in [1,2,3,4] at index ', last_index([1,2,3,4], 4) )
    print( '4 last in [4,2,3,4] at index ', last_index([4,2,3,4], 4) )
    print( '4 last in [1,2,3] at index   ', last_index([1,2,3], 4) )
    print( '4 last in [] at index        ', last_index([], 4) )
    
    print( '[1,2,3,4] is sorted?         ', is_sorted([1, 2, 3, 4]) )
    print( '[4,3,2,1] is sorted?         ', is_sorted([4, 3, 2, 1]) )
    print( '[1,2,3,2] is sorted?         ', is_sorted([1, 2, 3, 2]) )
    
if __name__ == '__main__':
    main()
    
