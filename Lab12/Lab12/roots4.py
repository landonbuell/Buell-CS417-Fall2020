"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab12
4 Nov 2020
"""

import math
import cmath

def real_root(a,b,c):
    disc = b*b - 4*a*c


    if a == 0:
        raise ValueError("Cannot have a = 0")
    if disc < 0:
        raise ValueError("no real roots")

    x1 = (-b + math.sqrt(disc))/(2*a)
    x2 = (-b - math.sqrt(disc))/(2*a)

    return (x1,x2)

def solve_quadratic(entry):
    fields = entry.split()
    if len(fields) != 3:        # not a,b,c,
        raise IndexError("Must have 3 arguments")

    a, b, c = [float(s) for s in fields]
    return real_root(a,b,c)

def main():
    while True:
        reply = input('Coefficients a b c : ')
        try:
            root = solve_quadratic(reply)
            print ('Root:',root)

        except ValueError as e:
            print ('Bad value! ', e)
        except IndexError as e:
            print ('Missing data! ', e)
        except Exception as e:
            print ('Something went wrong! ', e)

if __name__ == '__main__':
    main()

