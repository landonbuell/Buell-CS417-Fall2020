'''
Displays an ASCII image, and lets the user move a viewport
to show different parts of the image
'''
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

def display(img, x, y, width, height):
    '''
    Print the portion of the image within the viewport,
    which has top left (x y)
    and dimensions (width height)
    '''
    top = y - height
    left = x - width
    bottom = y
    right = x

    for row in range(top, bottom):
        line = ''
        for pixel in img[row][left : right]:
            if pixel == '0':
                line += '*'
            else:
                line += '.'
        print (line)

    print ('x y w h:',x,y,width,height)

def move_up(x, y, width, height, img_width, img_height):
    '''
    Move the viewport up a little bit
    '''
    y -= height // 4
    # Make sure the top of the viewport doesn't exceed
    # the top of the image
    top = y - height
    if top < 0:
        y = height
    return (x, y, width, height)

def move_down(x, y, width, height, img_width, img_height):
    '''
    Move the viewport down a little bit
    '''
    y += height // 4
    # Check if we've hit the bottom of the image
    if y > img_height:
        y = img_height - 1
    return (x, y, width, height)

def move_right(x, y, width, height, img_width, img_height):
    '''
    Move the viewport right
    '''
    x += width // 4
    # and make sure we don't go over the right edge
    if x > img_width:
        x = img_width
    return (x, y, width, height)

def move_left(x, y, width, height, img_width, img_height):
    '''
    Move the viewport left
    '''
    x -= width // 4
    # but don't move past the left edge
    left = x - width
    if left < 0:
        x = 0
    return (x, y, width, height)

def main():
    # First check if there is a command-line argument.
    # If not, use 'usa.txt'
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = 'usa.txt'
    map = read_img(map_name)

    (img_width, img_height, img) = read_img('usa.txt')

    print ('img w h:',img_width,img_height)

    width = 60
    height = 20

    x = img_width // 2 - width // 2
    y = img_height // 2 - height // 2

    while True:
        # This is the prompt-move loop
        # Show the viewport's portion of the image
        display(img, x, y, width, height)

        # Ask for a motion
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
            (x,y,width,height) = move_right(x, y, width, height,
                                            img_width, img_height)

        elif code == 'l':
            (x,y,width,height) = move_left(x, y, width, height,
                                           img_width, img_height)
        elif code == 'u':
            (x,y,width,height) = move_up(x, y, width, height,
                                         img_width, img_height)
        elif code == 'd':
            (x,y,width,height) = move_down(x, y, width, height,
                                           img_width, img_height)

if __name__ == '__main__':
    main()

