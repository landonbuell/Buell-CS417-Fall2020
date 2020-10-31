import sys

from list_node import List_Node


class Linked_List:
    '''
    An ordinary linked list, with both head and tail pointers.
    '''
    def __init__(self, data = None):
        '''
        List constructor.  Can be invoked in three ways:
        Linked_List() makes an empty list.
        Linked_List(<another Linked_List>) makes a copy of the other list.
        Linked_List(<a python list>) makes a list containing the list's values.
        '''
        self._head = None
        self._tail = None
        if data != None:
            if type(data) in (list, Linked_List):
                for x in data:
                    self.add_tail(x)
            else:
                raise ValueError("Can't build list from data of type "
                             + str(type(data)))

    def __str__(self):
        '''
        Printable version of the list.
        '''
        result = '('
        # Walk down the list, starting at head node
        current = self._head
        while current is not None:
            # add value to string
            result += str(current._value)
            if current._next is not None:
                # add a comma, but for last value
                result += ', '
            # advance
            current = current._next
        result += ')'
        return result

    def __repr__(self):
        '''
        Programmer-friendly printable version of the list.
        '''
        result = 'Linked_List(\n'
        current = self._head
        while current is not None:
            result += '   ' + repr(current)
            if current is self._head:
                result += ' == head'
            if current is self._tail:
                result += ' == tail'
            result += '\n'
            current = current._next
        result += ')'
        return result

    def first(self):
        '''
        Return first value, or None if list is empty
        '''
        if self.is_empty():
            return None
        else:
            return self._head._value

    def is_empty(self):
        '''
        Return True/False if list is/isn't empty
        '''
        return self._head == None

    def add_head(self, value):
        '''
        Add value, before first node.
        '''
        new_node = List_Node(value)
        new_node._next = self._head
        self._head = new_node
        if self._tail is None:
            # If list used to be empty, update tail pointer
            self._tail = self._head

    def add_tail(self, value):
        '''
        Add value into node after the tail
        '''

#        print('--------')
#        print('Entering add_tail(', value ,')')

        new_node = List_Node(value)

#        print('before, list is:')
#        print(repr(self))
#        print('new node:', repr(new_node))
        if self._tail is None:

#            print('add_tail: empty list')

            # Special case: empty list
            # Create a list with a ONE node
            self._tail = new_node
            self._head = new_node
        else:

#            print('add_tail: general case')

            # General case: add after tail, change tail pointer
            self._tail._next = new_node
            self._tail = new_node

#        print('after add_tail(', value, '):')
#        print(repr(self))

    def size(self):
        '''
        Length of list
        '''
        current = self._head
        n_nodes = 0
        while current is not None:
            n_nodes += 1
            current = current._next
        return n_nodes

    def find_node(self, value):
        '''
        Return the node that contains the given value,
        or None if it doesn't occur
        '''
        current = self._head
        while current is not None:
            if current._value == value:
                return current
            current = current._next
        return None

    def insert(self, value, index):
        '''
        Insert a value at a given index
        '''
        # Check if index is valid
        if index < 0 or index >= self.size():
            raise IndexError(str(index))

        if self._head == None:
            # Special case: empty list
            # Index will be zero (guaranteed), so just add to front
            self.add_head(value)
        else:
            # Walk down the list, stopping just before
            # insertion point
            prev = self._head
            for i in range(index - 1):
                prev = prev._next
            prev._next = List_Node(value, prev._next)

    def pop(self):
        '''
        Delete last node, return its value
        '''
        if self.is_empty():
            raise IndexError('pop from empty list')

        # Special case: list has ONE node
        if self._head == self._tail:
            # Save the value
            x = self._head._value
            # Make the list empty
            self._head = self._tail = None
        else:
            # General case (more than one node)
            # Walk down the list, stop just before the tail
            prev = self._head
            while prev._next != self._tail:
                prev = prev._next

            # save the value
            x = self._tail._value
            # delete old tail
            prev._next = None
            self._tail = prev
        return x

    def remove(self, x):
        '''
        Delete the node that holds x.  If list does not
        contain x, do nothing.
        '''
        prev = None
        victim = self._head
        while victim != None:
            if victim._value == x:
                if prev == None:
                    # No previous node (victim is head node)
                    self._head = victim._next
                else:
                    # bypass the victim
                    prev._next = victim._next
                # done deleting, get out
                break
            # didn't find x here, advance (and remember prev)
            prev = victim
            victim = victim._next


def main():
    pi = Linked_List([3, '.', 1, 4, 1])
    pi.add_head('A')
    pi.add_tail('Z')

    print ('pi:', pi)
    print ('pi in detail:')
    print (repr(pi))

    seven = pi.size()

    print ('Size should be 7  :', seven)
    print ('First             :', pi.first())
    node = pi.find_node(5)
    print ('Node with 5 is    :',repr(node))
    print ('Node with 23 is   :',pi.find_node(23))

    print ('popped            :', pi.pop())
    print ('After popping     :', pi)

    pi.remove('.')
    print ('after deleting ".":', pi)
    pi.remove(3)
    print ('after deleting 3  :', pi)

if __name__ == '__main__': main()
