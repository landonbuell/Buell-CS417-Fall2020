import sys

class List_Node:
    '''
    One node in the linked list.
    '''
    def __init__(self,
                 value=None,
                 next=None):
        self._value = value
        self._next  = next

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

class Linked_List:
    def __init__(self, orig = None):
        '''
        Constructor for the linked list.
        It takes an optional argument, which may be a regular
        python list, another Linked_List, or any container.
        If the argument is present, appends all its values to self.
        '''
        # Start with an empty list
        self._head = None
        # walk down orig, and append every element to THIS list.
        if orig != None:
            for x in orig:
                self.add_tail(x)

    def copy(self):
        '''
        Return a copy of this list.
        '''
        return Linked_List(self)

    def add_front(self, value):
        '''
        Add value to front of list
        '''
        self._head = List_Node(value, self._head)

    def add_tail(self, value):
        '''
        Add value to end of list
        '''
        if self._head == None:
            # special case for empty list
            self.add_front(value)
        else:
            # general case: walk down, until we reach tail node.
            current = self._head
            while current._next != None:
                current = current._next
            current._next = List_Node(value)

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
            prev = self._head
            for i in range(index - 1):
                prev = prev._next
            new_node = List_Node(value, prev._next)
            prev._next = new_node

    def __add__(self, other_list):
        '''
        Join two lists together: self + other_list
        '''
        result = Linked_List()
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
            current = self._head
            for i in range(index):
                current = current._next
            current._value = value

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
            current = self._head
            for i in range(index):
                current = current._next
            return current._value

    def __len__(self):
        '''
        Size of list
        '''
        # just walk down the list, counting nodes.
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current._next
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
            if index == 0:
                # special case: delete head node
                victim = self._head
                self._head = self._head._next
                del victim
            else:
                # general case: walk until you get to victim's predecessor.
                prev = self._head
                for x in range(index - 1):
                    prev = prev._next
                # remember the victim (we're returning it)
                victim = prev._next
                # now, set predecessor's next to BYPASS the victim.
                prev._next = victim._next
                del victim._value

    def __iter__(self):
        '''
        Generator for values in list
        '''
        current = self._head
        while current != None:
            yield current._value
            current = current._next

    def __reversed__(self):
        '''
        Reverse iterator for values in list
        '''
        raise NotImplementedError

    def __contains__(self, value):
        '''
        Containment test: True iff value is in list
        '''
        current = self._head
        while current != None:
            if current._value == value:
                return True
            current = current._next
        return False

    def __str__(self):
        '''
        User-friendly stringification of list
        '''
        result = '['
        current = self._head
        while current != None:
            result += str(current._value)
            current = current._next
            if current != None:
                result += ', '
        result += ']'
        return result

    def __repr__(self):
        '''
        Programmer-friendly stringification of list.
        Useful for debugging.
        '''
        prev_nodes = set()
        result = 'Linked_List(\n'
        current = self._head
        while current != None:
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
        result += ')'
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
    ints = Linked_List()

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

    words = Linked_List(['three',
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
