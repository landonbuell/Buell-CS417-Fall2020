"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab12
4 Nov 2020
"""

import math

def real_root(a,b,c):
    if a == 0:
        return (0,False)
    disc = b*b - 4*a*c   
    if disc < 0:
        return (0, False)
    return ((-b - math.sqrt(disc))/(2*a), True)

def solve_quadratic(entry):
    fields = entry.split()
    if len(fields) != 3:
        return (0,False)
    a, b, c = [float(s) for s in fields]
    (root, success) = real_root(a,b,c)
    if success:
        return (root, True)
    else:
        return (root, False)

def main():
    while True:
        reply = input('Coefficients a b c : ')
        (root, success) = solve_quadratic(reply)
        if success:
            print ('Real root:', root)
        else:
            print ('Something went wrong.  Try again')

if __name__ == '__main__':
    main()

