"""
Landon Buell
Alejo hausner
CS 417.01 - Assignment 05
13 October 2020
"""

import math

class Complex:
    '''
    Our own implementation of a complex number
    '''
    def __init__(self, r_part: float=0.0, i_part: float=0.0):
        '''
        Constructor.  No need to change this.
        '''
        self._real = r_part
        self._imag = i_part

    def plus(self, other: "Complex") -> "Complex":
        '''
        Add self + other, and return the resulting
        complex number.

        No need to change this!
        '''
        sum_real = self._real + other._real
        sum_imag = self._imag + other._imag
        return Complex(sum_real, sum_imag)

    def minus(self, other: "Complex") -> "Complex":
        '''
        Subtract self - other, and return the resulting
        complex number.

        YOU MUST CHANGE THIS!
        '''
        other.times(Complex(-1,0))      # multiply by -1
        return self.plus(other)         # add

    def times(self, other: "Complex") -> "Complex":
        '''
        Multiply self x other, and return the resulting
        complex number

        YOU MUST CHANGE THIS!
        '''
        # The following line needs to be replaced
        new_real = self._real*other._real - self._imag*other._imag
        new_imag = self._real*other._imag + self._imag*other._real
        return Complex(new_real,new_imag)

    def over(self, other: "Complex") -> "Complex":
        '''
        Divides self / other, and returns the resulting
        complex number

        YOU MUST CHANGE THIS!
        '''
        denom = other._real**2 + other._imag**2
        new_real = self._real*other._real + self._imag*other._imag
        new_imag = self._imag*other._real + self._real*other._imag
        new_real /= denom
        new_imag /= denom
        return Complex(new_real,new_imag)

    def conjugate(self) -> "Complex":
        '''
        Returns the conjugate of self, which is another
        complex number.
        Its real part is self._real, and
        its imaginary part is -self._imag  (note the minus!)

        YOU MUST CHANGE THIS!
        '''
        return Complex(self._real,self._imag*-1)

    def magnitude(self) -> float:
        '''
        Returns the magnitude of self, which uses the
        pythagorean theorem: it's
        the square root of
           the sum of
               the square of the real part +
               the square of the imaginary part

        YOU MUST CHANGE THIS!
        '''
        norm_sq = self._real**2 + self._imag**2
        return math.sqrt(norm_sq)

    def real(self) -> float:
        '''
        Returns the real part.  No need to change this.
        '''
        return self._real

    def imag(self) -> float:
        '''
        Returns the imaginary part.
        YOU MUST CHANGE THIS!
        '''
        return self._imag

    def __str__(self) -> str:
        '''
        Returns a string version of self, made up of
        str(self._real),
        a space
        a plus sign
        a space
        str(self._imag)
        the letter 'i'

        YOU MUST CHANGE THIS!
        '''
        # The following line needs to be replaced
        return str(self._real)+" + i"+str(self._imag)

    def equals(self, other: "Complex") -> bool:
        '''
        Returns True/False if both the real and imaginary parts of self
        are the same as those parts of other

        YOU MUST CHANGE THIS!
        '''
        # The following line needs to be replaced
        return (self._real == other._real) and (self._imag == other._imag)


def main():
    '''
    This is testing code for the Complex class.

    Modules can be used in two ways:
    1. import <module name>     (from within another python program)
    2. python <module name>.py  (from the command line)

    In the first version, __name__ will be the module name.
    In the second version __name__ will be '__main__'.

    We use the second version to trigger this testing code.
    '''
    one = Complex(1)
    two = Complex(1,0)
    i = Complex(0,1)
    oneone = Complex(1,1)

    print ('one * one:',one.times(one))
    print ('one *   i:',one.times(i))
    print ('one + one:',one.plus(one))
    print ('conj(1+i):',oneone.conjugate())
    print ('mag(1+i) :',oneone.magnitude())
    print ('(1+i) + (1+i):',oneone.plus(oneone))
    print ('(1+i) * (1+i):',oneone.times(oneone))
    print ('(2+4i) / (1+i):',Complex(2,4).over(Complex(1,1)))
    print ('(1+i) * i / (1-i):',oneone.times(i).over(Complex(1,-1)))

if __name__ == '__main__':
    # Run the test code, because we RAN the module.
    main()

else:
    # __name__ is 'complex', because we IMPORTED the module.
    # so don't run any code, just bring in the class and its methods.
    pass


