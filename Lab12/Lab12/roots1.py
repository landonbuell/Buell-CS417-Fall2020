import math

def real_root(a,b,c):
    disc = b*b - 4*a*c
    return (-b - math.sqrt(disc)) / (2*a)

def solve_quadratic(entry):
    a, b, c = [float(x) for x in entry.split()]
    root = real_root(a,b,c)
    return root

def main():
    while True:
        print ("Let's solve a quadratic equation a x^2 + b x + c = 0")
        reply = input('Enter coefficients a b c on one line : ')
        root = solve_quadratic(reply)
        print ('Root:',root)

if __name__ == '__main__':
    main()

