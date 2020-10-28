"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab13
28 October 2020
"""

from linked_list import Linked_List

class Enhanced_List(Linked_List):

    '''
    Constructor.  Notice how we call the constructor
    of the parent class.
    '''
    def __init__(self, orig = None):
        # Can this be done as super().__init__(....) ???
        Linked_List.__init__(self, orig)

    '''
    Add up values in the list, and return the total
    '''
    def sum(self):
        _sum = 0                # init sum
        current = self._head    # init location
        while current is not None:
            _sum += current._value  # add val
            current = current._next # incr
        return _sum
    '''
    Get the average of the values in the list
    '''
    def average(self):
        # Compute sum of list, divide by number of nodes
        return self.sum()/self.size()

    '''
    Make and return a new list, with values in reverse order.
    '''
    def reversed(self):
        _result = Linked_List()     # init empty list
        current = self._head        # init start
        while current is not None:
            _result.add_head(current._value)
            current = current._next # incr
        return _result

    '''
    Return the index where the value occurs in the list.
    Return -1 if value does not occur in list.
    '''
    def index_of(self, value):
        _index = 0
        current = self._head
        while current is not None:
            if (current._value == value):   # what we're looking for
                return _index
            _index += 1
            current = current._next
        # this might break if the list is empty
        return -1

    '''
    Return the value at the given index.
    Return None if index is out of bounds.
    '''
    def at_index(self, index):
        if (index  < 0):        # neg num
            return None
        elif (index > self.size()): # out of range
            return None 
        else:
            _cntr = 0                   # counter
            current = self._head        # init start
            while current is not None:
                if (_cntr == index):    # coutner is index
                    return current._value      # get value here
                _cntr += 1
                current = current._next
            


def main():
    a_list = Enhanced_List([3, 1, 4, 1, 5, 9])
    print ('a_list          :', a_list)
    print ('sum(a_list)     :', a_list.sum())
    print ('avg(a_list)     :', a_list.average())
    print ('a_list reversed :', a_list.reversed())
    print ('index_of(5)     :', a_list.index_of(5))
    print ('index_of(0)     :', a_list.index_of(0))
    print ('at_index(1)     :', a_list.at_index(1))
    print ('at_index(-1)    :', a_list.at_index(-1))

if __name__ == '__main__':
    main()

