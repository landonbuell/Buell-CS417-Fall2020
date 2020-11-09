"""
Landon Buell
Alejo Hausner
CS 417.01 - Asn07
3 Nov 2020
"""

import sys

class List_Node:
    '''
    One node in the linked list.
    '''
    def __init__(self,
                 value=None,
                 next=None,
                 prev=None):
        self._value = value
        self._next  = next
        self._prev = prev

    def __str__(self):
        return '(' + str(self._value) + ')'

    def __repr__(self):
        result = '('
        result += '(@' + str(id(self)) + ' ' + repr(self._value) + ') -> '
        if self._next == None:
            result += 'None)'
        else:
            result += str(id(self._next))
            result += ')'
        return result

# Linked list class

class Double_List:
    def __init__(self, orig = None):
        '''
        Constructor for the linked list.
        It takes an optional argument, which may be a regular
        python list, another Double_List, or any container.
        If the argument is present, appends all its values to self.
        '''
        # Start with an empty list 
        self._head = List_Node()
        self._tail = List_Node()
        self._head._next = self._tail
        self._tail._prev = self._head

        # walk down orig, and append every element to THIS list.
        if (orig != None): 
            if (type(orig) == list):         # list type
                for x in orig:
                    self.add_tail(x)
            elif (type(orig) == List_Node):  # list Node 
                self.add_tail(orig._value)
            elif (type(orig) == Double_List):# Double List
                raise NotImplementedError()
            else:
                raise NotImplementedError()



    def copy(self):
        '''
        Return a copy of this list.
        '''
        return Double_List(self._head)

    def add_front(self, value):
        '''
        Add value to front of list
        '''
        # create new node w/ links
        new = List_Node(value,self._head._next,self._head) 
        # Conenct to head/tail
        self._head._next._prev = new          
        self._head._next = new
        return self._head

    def add_tail(self, value):
        '''
        Add value to end of list
        '''
        new = List_Node(value,self._tail,self._tail._prev)
        self._tail._prev._next = new
        self._tail._prev = new
        return self._head

    def insert(self, value, index):
        '''
        Insert value into list, at given index.
        '''
        # first, some error checks
        if type(index) != int:
            raise TypeError
        elif index > len(self):
            raise IndexError
        elif index == len(self):
            # special case: empty list
            self.add_tail(value)
        else:
            # general case. Walk down the list, the correct number of steps.
            new = List_Node(value)
            curr = self._head
            for i in range(index - 1):
                curr = curr._next     
            curr._next._prev = new
            new._next = curr._next
            curr._next = new
            new._prev = curr
        return self._head

    def is_empty(self):
        '''
        Return True/False if list is or isn't empty
        '''
        if len(self) == 0:  # no nodes
            return True     # empty
        else:               # nodes
            return False    # not empty
                           
    def __add__(self, other_list):
        '''
        Join two lists together: self + other_list
        '''
        result = Double_List()
        for x in self:
            result.add_tail(x)
        for x in other_list:
            result.add_tail(x)
        return result

    def __setitem__(self, index, value):
        '''
        Modify entry in list, at given index
        '''
        # first, check that index is OK
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
           # index is good. Walk down the list, the correct number of times.
            current = self._head._next
            for i in range(index):
                current = current._next
            current._value = value
        return self._head

    def __getitem__(self, index):
        '''
        Retrieve entry in list at given index
        '''
        # first, check that index is OK
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
           # index is good. Walk down the list, the correct number of times.
            current = self._head._head
            for i in range(index):
                current = current._next
            return current._value

    def __len__(self):
        '''
        Size of list
        '''
        # just walk down the list, counting nodes.
        curr = self._head._next
        count = 0
        while curr != self._tail:
            count += 1
            curr = curr._next
        return count

    def __delitem__(self, index):
        '''
        Remove entry in list, at given index
        '''
        # first, check if index is OK
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
            # index is OK.
            curr = self._head._next
            for i in range (index):
                curr = curr._next
            curr._prev._next = curr._next # overwrite next
            curr._next._prev = curr._prev # overwrite prev
            return self._head

    def __iter__(self):
        '''
        Generator for values in list
        '''
        curr = self._head._next
        while curr != self._tail:
            yield curr._value
            curr = curr._next

    def __reversed__(self):
        '''
        Reverse iterator for values in list
        '''
        curr = self._tail._prev     # last node before tail
        while curr != self._head:   # while not at head
            yield curr._value
            curr = curr._prev       # work our way backwards
        

    def __contains__(self, value):
        '''
        Containment test: True iff value is in list
        '''
        current = self._head._next      # start after head
        while current != self._tail:
            if current._value == value: # is value?
                return True             # break, return true
            current = current._next
        return False                    # got here? not in list

    def __str__(self):
        '''
        User-friendly stringification of list
        '''
        result = '['
        current = self._head._next
        while current != self._tail:
            result += str(current._value)
            current = current._next
        result += ']'
        return result

    def __repr__(self):
        '''
        Programmer-friendly stringification of list.
        Useful for debugging.
        '''
        prev_nodes = set()
        result = 'Double_List(\n'
        current = self._head
        while current != self._tail:
            prev_nodes.add(current)
            result += '  ' + repr(current)
            if current == self._head:
                result += ' == head'
            result += '\n'
            if current._next in prev_nodes:
                print ('ERROR: circular reference in node:',repr(current))
                break
            else:
                current = current._next
        result += '  ' + repr(self._tail)
        result += ' == tail'
        result += ' )'
        return result

    '''
    Checks for back-links in list.
    Call this often!
    '''
    def has_back_links(self):
        prev_nodes = set()
        current = self._head
        while current != None:
            prev_nodes.add(current)
            if current._next in prev_nodes:
                return True
        return False

def main():
    ints = Double_List()

    print ('empty list has', len(ints), 'values')
    print ('initial empty list:', ints)
    print ('initial empty list repr:', repr(ints))

    ints.add_tail(1)
    ints.add_front(4)
    ints.add_tail(6)
    ints.add_front(1)
    ints.add_front(3)
    ints.insert('.', 1)

    print ('After adding 6 values, length:', len(ints))
    print ('List values:', ints)
    print ('List repr:', repr(ints))

    print ('Iterating through ints:')
    for x in ints:
        print (x, end=' ')
    print ()

    print ('Reverse iterating through ints:')
    try:
        for x in reversed(ints):
            print (x, end=' ')
        print()
    except NotImplementedError:
        print ('REVERSE ITERATOR NOT IMPLEMENTED')

    del ints[3]

    print ('After removing 4th entry:', ints)
    print ('After removing 4th entry, repr is:')
    print (repr(ints))

    words = Double_List(['three',
                         'point',
                         'one',
                         'four',
                         'one',
                         'six'])
    words[0] = 'drei'
    words[1] = 'dot'

    print ('words:', words)
    print ('copy of words:', words.copy())

    combined = ints + words
    print ('ints + words:', combined)


if __name__ == '__main__':
    main()
