import sys
import os
from complex import Complex

def julia_converges(x: float, y: float,
                    max_steps: int, cx: float, cy: float) -> bool:
    '''
    Returns True/False if the point (x y) does/doesn't meet the
    convergence condition.
    Method:
    1. Create the complex value z = Complex(x,y)
    2. Create the complex value c = Complex(cx,cy)
    3. Enter a loop, in which you update z:
       z = z.times(z).plus(c)
    4. Exit the loop when z gets too big (magnitude > 2: no convergence), or
       the loop has run max_steps times (converges).
    '''
    # Replace the following line
    return True

def show_set(left: float, top: float,
             width: float, height: float,
             c_real: float, c_imag: float) -> None:
    '''
    Draws a picture of a region of the Julia set
    The region is a rectangle, with:
    x between left and left+width,
    y between top and top-height
    '''
    os.system('cls||clear')

    display_columns = 70
    display_rows = 22

    # The step sizes
    dx = width / display_columns
    dy = height / display_rows

    # Initial value of y
    y = top
    for row in range(display_rows):
        # initial value of x, for this row
        x = left
        for col in range(display_columns):
            # Call julia_converges to see if this (x y)
            # meets the condition.
            if julia_converges(x,y, 100, c_real, c_imag):
                # It does!
                sys.stdout.write('*')
            else:
                # It does not
                sys.stdout.write('.')
            # Advance to the right
            x += dx
        # line done, start a new line
        sys.stdout.write('\n')
        y -= dy

def main():
    '''
    Show the Julia set
    '''
    if len(sys.argv) == 3:
        # User gave us the complex number c, on the command line.
        c_real = float(sys.argv[1])
        c_imag = float(sys.argv[2])
    else:
        # Use default c, for an interesting Julia set.
        c_real = 0.3
        c_imag = 0.5

    x_min = -2.0
    y_max = +1.0
    width = 4
    height = 2
    while True:

        # Un-comment the next line, for debugging purposes
        print ('L B W H :',x_min, y_max, width, height)

        show_set(x_min, y_max, width, height, c_real, c_imag)
        reply = input('In, Out, Right, Left, Up, Down, Quit? ')
        if len(reply) == 0:
            continue
        code = reply.lower()[0]

        if code == 'r':
            x_min += width / 4

        elif code == 'l':
            # Replace this line
            dummy = 0

        elif code == 'u':
            # Replace this line
            dummy = 0

        elif code == 'd':
            # Replace this line
            dummy = 0

        elif code == 'i':
            # Replace this line
            dummy = 0

        elif code == 'o':
            # Replace this line
            dummy = 0

        elif code == 'q':
            break

if __name__ == '__main__':
    main()

