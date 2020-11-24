
class Stack:
    """
    A simple push/pop stack, implemented with a python list
    """
    def __init__(self):
        self._data = []

    def push(self, x):
        """Add x to the stack."""
        self._data.append(x)

    def pop(self):
        """Remove (and return) the top of the stack."""

        if self.empty():
            raise IndexError('Empty stack')
        return self._data.pop()

    def top(self):
        """Return the top of the stack, but don't pop."""

        if self.empty():
            raise IndexError('Empty stack')
        return self._data[-1]

    def empty(self):
        """Return True/False if the stack is/isn't empty."""
        return len(self._data) == 0

    def __len__(self):
        """Return # of values on stack."""

        return len(self._data)

    def __iter__(self):
        """Visit all the values on the stack."""

        for x in self._data:
            yield x

    def __str__(self):
        """Stringified version of the stack"""

        return str(self._data)

def main():
    """
    Code to test the above class.
    """
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print( '30 on top?', (s.top() == 30) )
    print( 'stack:', s)
    x = s.pop()
    print( 'Popped 30?', (x == 30) )
    s.pop()
    s.pop()
    print( 'After popping everything, is stack empty?', s.empty() )
    exception_thrown = False
    try:
        s.pop()
    except IndexError:
        exception_thrown = True
    if exception_thrown:
        print( 'Popping empty stack raises exception as expected' )
    else:
        print( 'pop on empty stack raises no exception!' )

if __name__ == '__main__':
    main()
