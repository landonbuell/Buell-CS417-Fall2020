"""
Landon Buell
Alejo Hausner
CS 414.01 - Lab14
30 October 2020
"""

import sys

from list_node import List_Node

class Sentinel_List:
    '''
    A linked list with sentinel nodes.
    The head and tail pointers aren't None; they refer to actual nodes.
    Those actual nodes are "sentinels": they don't hold useful data,
    but protect the ends of the list.  They make many operations simpler.
    '''

    def __init__(self, data = None):
        '''
        List constructor.  Can be invoked in three ways:
        Sentinel_List() makes an empty list.
        Sentinel_List(<another Sentinel_List>) makes a copy of the other list.
        Sentinel_List(<a python list>) makes list containing data's values.
        '''
        # EXERCISE 0 (done for you): create sentinel nodes
        self._head = List_Node()
        self._tail = List_Node()
        # link sentinels together.
        self._head._next = self._tail

        if data != None:
            if type(data) in (list, Sentinel_List):
                for x in data:
                    self.add_tail(x)
            else:
                raise ValueError("Can't build list from data of type "
                             + str(type(data)))

    def __str__(self):
        '''
        Printable version of the list.
        '''

        # EXERCISE 1: skip over the sentinel nodes.
        # Modifications:
        # a) start at self._head._next
        # b) keep going while current isn't self._tail
        # c) change test for adding comma

        result = '('
        # Walk down the list, starting at head node
        current = self._head._next
        while current is not self._tail:
            # add value to string
            result += str(current._value)
            if current._next is not self._tail:
                # add a comma, except for last value
                result += ', '
            # advance
            current = current._next
        result += ')'
        return result

    def __repr__(self):
        '''
        Programmer-friendly printable version of the list.
        '''

        # DON'T CHANGE THIS.
        # If you are a programmer, you WANT to see the sentinel nodes

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

        # EXERCISE 2: skip over head sentinel
        # Modification:
        # - get value of self._head._next, instead of self._head
        if self.is_empty():
            return None
        else:
            return self._head._next

    def is_empty(self):
        '''
        Returns True/False if list is/isn't empty
        '''

        # EXERCISE 3: Check if head._next points to tail
        # Modification:
        # - compare self._head._next to self._tail, not to self._head to None
        return self._head._next == self._tail

    def add_head(self, value):
        '''
        Add value into node just after head sentinel
        '''

        # EXERCISE 4: No special case for empty list
        # Modifications:
        # a) new_node._next should point to self._head._next, instead of self._head
        # b) self._head._next should be changed, instead of self._head
        # c) DELETE code that checks an empty tail.

        new_node = List_Node(value)
        new_node._next = self._head._next
        self._head._next = new_node
        return self._head

    def add_tail(self, value):
        '''
        Add value into node at the end of the list
        '''

        # EXERCISE 5: Insert before tail sentinel
        # Modifications:
        # a) set new_node._next = self._tail
        # b) delete all code after that (it's all different)
        # c) walk down the list:
        #    - prev starts at self._head
        #    - keep going while prev._next is not self._tail
        #    - after loop, prev._next should now be new_node

        new_node = List_Node(value) # Keep this line
        # Put a) here, and remove the lines below this one.
        new_node._next = self._tail

        _prev = self._head
        while _prev._next is not self._tail:
            _prev = _prev._next
        _prev = new_node
        return self._head
        
    def size(self):
        '''
        Length of list
        '''

        # EXERCISE 6: skip sentinel nodes
        # Modifications: (just like in __str__(self) method)

        n_nodes = 0
        _curr = self._head._next
        while _curr is not self._tail:
            n_nodes += 1
            _curr = _curr._next
        return n_nodes

    def find_node(self, value):
        '''
        Return the node that contains the given value,
        or None if it doesn't occur
        '''

        # EXERCISE 7: skip sentinels
        # Modifications: (just like in __str__(self) method)

        _curr = self._head._next
        while _curr is not self._tail:
            if _curr._value == value:
                return _cur
            _curr = _curr._next
        return None

    def insert(self, value, index):
        '''
        Insert a value at a given index
        '''
        # Check if index is valid
        if index < 0 or index >= self.size():
            raise IndexError(str(index))

        # EXERCISE 8: skip head sentinel
        # Modifications:
        # a) Delete the special-case code (empty list)
        # b) Delete the else: (of course)
        # c) De-indent the code after the else (of course)
        # d) Take one more step: (range(index) instead of range(index-1))
        
        # Walk down the list, stopping just before
        # insertion point
        prev = self._head
        for i in range(index):
            prev = prev._next
        prev._next = List_Node(value, prev._next)

    def pop(self):
        '''
        Delete last node, return its value
        '''
        if self.is_empty():
            raise IndexError('pop from empty list')

        # EXERCISE 9: Delete just before tail sentinel
        # Modifications:
        # a) Delete the special-case code (one-node list)
        # b) Delete the else: (of course)
        # c) Keep walking while prev._next._next is not self._tail
        # d) Save prev._next._value, not self._tail._value
        # e) prev._next should now be self._tail (bypassing the deleted node)
        # f) Don't change self._tail!  Delete that line.

        # General case (more than one node)
        # Walk down the list, stop just before the tail
        prev = self._head
        while prev._next._next != self._tail:
            prev = prev._next

        # save the value
        x = prev._next._value
        # delete old tail
        prev._next = self._tail
        return x

    def remove(self, x):
        '''
        Delete the node that holds x.
        If x is not in the list, do nothing.
        '''

        # EXERCISE 10 (bonus): Figure this out yourself.

        prev = None
        

def main():
    pi = Sentinel_List([3, '.', 1, 4, 1])
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
