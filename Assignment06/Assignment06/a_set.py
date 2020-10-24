"""
Landon Buell
Alejo Hausner
CS 417.01 - Asn06
24 October 2020
"""

import copy

class a_set:
    '''
    An implementation of a set.
    This is a collection of values, with no repetitions
    '''
    def __init__(self, orig=None):
        '''
        Constructor.  If the (optional) orig argument is present,
        copy its values into self._data
        '''
        if orig == None:
            self._data   = [] # empty set
        elif type(orig) == list:
            self._data = []
            for x in orig:
                self.add(x)
        elif type(orig) == type(self):
            self._data = copy.copy(orig._data)

    def copy(self):
        '''
        Return a copy of this set.
        '''
        result = a_set(self)
        return result

    def __iter__(self):
        '''
        Generator that visits all the values in this set
        '''
        next = 0
        while next < len(self._data):
            yield self._data[next]
            next += 1

    ############################################################
    # You must implement the following methods:

    def add(self, value):
        '''
        Add this value to the end of the list.
        If it's already in the list, do nothing.
        '''
        self._data.append(value)
        return self

    def __contains__(self, value):
        '''
        Return True/False if value occurs/doesn't occur in the list
        '''
        # REPLACE THE NEXT LINE
        if value in self._data:
            return True
        else:
            return False

    def remove(self, value):
        '''
        If value is in the list, pop it.
        If not, raise KeyError

        RETURN the value that you just removed.
        '''
        try:
            self._data.remove(value)
        except:
            raise KeyError()
        return value

    def union(self, other):
        '''
        Return a new a_set, which contains elements that
        occur in self, plus elements that occur in other
        '''
        unionSet = a_set()
        for i in self._data:    # iter through this set
            unionSet.add(i)     # add to union
        for j in other._data:   # iter through other set
            unionSet.add(i)     # add to union
        return unionSet         # return 


    def intersection(self, other):
        '''
        Return a new a_set, which contains all the values
        that occur in BOTH self and other
        '''
        intersectSet = a_set()
        for i in self._data:        # in the current set
            if i in other._data:    # if in the other set
                intersectSet.add(i) # add to new set
        return intersectSet         # return the new set

    def difference(self, other):
        '''
        Return a new a_set, which contains all the values
        that occur in self, but do NOT occur in other
        '''
        diffSet = a_set()
        for i in self._data:            # in the current set
            if i not in other._data:    # if NOT in the other set
                diffSet.add(i)          # add to new set
        return diffSet                  # return the new set

    def issubset(self, other):
        '''
        Return True/False if self is/isn't a subset of other.
        A is a subset of B if, for every x in A, x is also in B.
        '''
        subset = True               # set cond
        for i in other._data:       # other set
            if i not in self._data: # not in this set
                return False        # not a subset, break
        return subset               # return cond

    def __len__(self):
        '''
        Return number of values (it's a one-liner)
        '''
        return len(self._data)

    def __repr__(self):
        '''
        Return a string describing the set.
        Example: if self contains {1, 3, 4}, this should
                 return the string 'a_set(1, 3, 4)'
        Notice that the last element has no comma after it!
        '''
        if self.__len__() == 0:     # null set
            return "a_set( )"
        else:
            output = "a_set("
            for i in range(self.__len__() - 1): # each elem (not last)
                output += str(self._data[i])+", "
            output += str(self._data[-1])+")"   # add last, close paran
            return output

    def __str__(self):
        '''
        Return a user-friendly string describing the set.
        Example: if self contains {1, 3, 4}, this should
                 return the string '{1, 3, 4}'
        Notice that each element is followed by a comma, space,
        but not the last element.
        '''
        if self.__len__() == 0:     # null set
            return "{ }"
        else:
            output = "{"
            for i in range(self.__len__() - 1): # each elem (not last)
                output += str(self._data[i])+", "
            output += str(self._data[-1])+"}"   # add last, close bracket
            return output

def main():
    yes_no = {True:'yes', False:'no '}

    my_set = a_set()
    print( 'Empty set:', my_set )

    print('\nTesting "add()":')

    A = a_set([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    B = a_set([8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2])

    print('\nTesting "__str__":')

    print( '  A =', A )
    print( '  B =', B )

    print('\nTesting "__repr__":')
    print( '  repr(A) =', repr(A) )
    print( '  repr(B) =', repr(B) )


    print('\nTesting "remove":')

    A.remove(3)
    A.remove(9)
    B.remove(8)
    B.remove(7)

    print( '  After deletions:' )
    print( '  A =', A )
    print( '  B =', B )

    try:
        A.remove(99)
        print( '  BAD: No exception raised when deleting absent key!')
    except KeyError:
        print( '  CORRECT: Exception raised when deleting absent key' )

    print( '\nTesting "contains":')

    tf_to_yn = {True:"Y", False:"."}

    print("        ", end = "")
    for x in range(10):
        print("{:>4}".format(x), end="")
    print()
    print("  in A? ", end = "")
    for x in range(10):
        print("{:>4}".format(tf_to_yn[x in A]), end="")
    print()
    print("  in B? ", end = "")
    for x in range(10):
        print("{:>4}".format(tf_to_yn[x in B]), end="")
    print()

    print('\nTesting "union":')

    print( '  A union B =', A.union(B) )

    print('\nTesting "intersection":')

    print( '  A intersect B =', A.intersection(B))

    print('\nTesting "difference":')

    print( '  A minus B =', A.difference(B))
    print( '  B minus A =', B.difference(A))

    print('\nTesting "issubset":')
    print( '  A subset of B?', A.issubset(B))
    print( '  B subset of A?', B.issubset(A))
    print( '  A subset of A?', A.issubset(A))

    print( '\nTesting "__len__":')
    print( '  len(A) =', len(A))
    print( '  len(B) =', len(B))

if __name__ == '__main__':
    main()

