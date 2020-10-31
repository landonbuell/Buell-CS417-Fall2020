'''
List_Node is used by the Linked_List class.
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
