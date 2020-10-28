import sys

# Linked list class

class Linked_List:
    '''
    List_Node is an inner class of the Linked_List class.
    It stores a value, and a pointer to the next List_Node.
    Note the __repr__ method, which shows the addresses in
    the next pointers, so you can compare several nodes and
    verify that they are indeed linked together correctly.
    '''
    class List_Node:
        def __init__(self, value = None, next = None):
            self._value = value
            self._next = next

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

    '''
    List constructor.  Can be invoked in three ways:
    Linked_List() makes an empty list.
    Linked_List(<another Linked_List>) makes a copy of the other list.
    Linked_List(<a python list>) makes a list containing the list's values.
    '''
    def __init__(self, data = None):
        self._head = None
        self._tail = None
        if data != None:
            if type(data) in (list, Linked_List):
                for x in data:
                    self.add_tail(x)
            else:
                raise ValueError("Can't build list from data of type "
                             + str(type(data)))

    '''
    Printable version of the list.
    '''
    def __str__(self):
        result = '('
        current = self._head
        while current is not None:
            result += str(current._value)
            if current._next is not None:
                result += ', '
            current = current._next
        result += ')'
        return result

    '''
    Programmer-friendly printable version of the list.
    '''
    def __repr__(self):
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

    '''
    Return first value, or None if list is empty
    '''
    def first(self):
        if self._head is None:
            return None
        else:
            return self._head._value

    '''
    Return tail's value, or None if list is empty
    '''
    def last(self):
        if self._tail is None:
            return None
        else:
            return self._tail._value

    '''
    Add value into node before the head
    '''
    def add_head(self, value):
        self._head = self.List_Node(value, self._head)
        if self._tail is None:
            self._tail = self._head

    '''
    Add value into node after the tail
    '''
    def add_tail(self, value):
        new_node = self.List_Node(value)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

    '''
    Length of list
    '''
    def size(self):
        current = self._head
        n_nodes = 0
        while current is not None:
            n_nodes += 1
            current = current._next
        return n_nodes


    '''
    Return the node that contains the given value,
    or None if it doesn't occur
    '''
    def find_node(self, value):
        current = self._head
        while current is not None:
            if current._value == value:
                return current
            current = current._next

def main():
    pi = Linked_List([3, '.', 1, 4, 1, 5])
    pi.add_tail(9)
    pi.add_head('start')
    pi.add_tail('done!')

    print ('pi:', pi)
    print ('pi in detail:')
    print (repr(pi))

    nine = pi.size()

    print ('Should be 9       :', nine)
    print ('First and last    :', pi.first(), pi.last())
    pi.add_head('PI =')
    pi.add_tail( '...')
    print ('After adds        :', pi)
    print ('Size should be 11 :', pi.size())
    node = pi.find_node(5)
    print ('Node with 5 is    :',repr(node))
    print ('Node with 23 is   :',pi.find_node(23))

if __name__ == '__main__': main()
