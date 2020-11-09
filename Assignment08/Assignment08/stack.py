
class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if self.empty():
            raise IndexError('Empty stack')
        return self._data.pop()

    def top(self):
        if self.empty():
            raise IndexError('Empty stack')
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        for x in self._data:
            yield x
            
    def __str__(self):
        return str(self._data)

def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print ('30 on top?', (s.top() == 30))
    x = s.pop()
    print ('Popped 30?', (x == 30))
    s.pop()
    s.pop()
    print ('Stack empty?', s.empty())
    exception_thrown = False
    try:
        s.pop()
    except IndexError:
        exception_thrown = True
    if exception_thrown:
        print ('Threw exception as expected')
    else:
        print ('pop on empty stack throws no exception!')

if __name__ == '__main__':
    main()
