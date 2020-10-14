'''
Displays an ASCII image, and lets the user move a viewport
to show different parts of the image.

Uses an object-oriented approach: The Viewport class handles most
of the details.
'''

from viewport import Viewport
import sys

def read_img(filename):
    '''
    Read the image from a text file
    '''
    handle = open(filename, 'r')
    img = [line.rstrip('\r\n') for line in handle.readlines()]
    img_width = int(img[0])
    img_height = int(img[1])
    return (img_width, img_height, img[2:])

def main():
    # First check if there is a command-line argument.
    # If not, use 'usa.txt'
    if len(sys.argv) == 2:
        img_name = sys.argv[1]
    else:
        img_name = 'usa.txt'

    (img_width, img_height, img) = read_img(img_name)

    # Initialize the viewport
    port = Viewport(60,20)
    port.set_img(img_width, img_height)

    while True:
        # This is the prompt-move loop
        # Show the viewport's portion of the image
        port.display(img)
        print (port)

        reply = input('Right, Left, Up, Down, Quit? ')
        # Do some input validation
        input_OK = True
        if len(reply) > 0:
            code = reply.lower()[0]
            if code not in 'udlrq':
                input_OK = False
        else:
            input_OK = False

        if not input_OK:
            print ('u d r l q only, please!')
            continue

        if code == 'q':
            break

        elif code == 'r':
            port.move_right()
        elif code == 'l':
            port.move_left()
        elif code == 'u':
            port.move_up()
        elif code == 'd':
            port.move_down()

if __name__ == '__main__':
    main()
