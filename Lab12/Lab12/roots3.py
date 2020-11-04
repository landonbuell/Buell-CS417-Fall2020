"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab12
4 Nov 2020
"""

import math

def root(a,b,c):
    if a == 0:
        return (0,2)
    disc = b*b - 4*a*c
    if disc < 0:
        return (0, 1)
    return ((-b - math.sqrt(disc))/(2*a), 0)

def solve_quadratic(entry):
    fields = entry.split()
    if len(fields) != 3:
        return (0,3)
    a, b, c = [float(s) for s in fields]
    (root, result) = real_root(a,b,c)
    if result == 0:
        return (root, 0)
    else:
        return (root, result)

def main():
    while True:
        reply = input('Coefficients a b c : ')
        (root, result) = solve_quadratic(reply)
        if result == 0:
            print ('Real root:', root)
        elif result == 1:
            print ('All roots are complex')
        elif result == 2:
            print ('a is zero (this is not a quadratic equation)')
        elif result == 3:
            print ('Missing coefficients')
        else:
            print ('Unknown result code:', result)

if __name__ == '__main__':
    main()

