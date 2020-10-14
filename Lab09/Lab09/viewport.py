"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab09
14 Oct 2020
"""

# No Imports

'''
A viewport into a larger rectangular ASCII picture
'''
class Viewport:
    """ Viewport Class """
    
    def __init__(self, width, height):
        """ Initialize instance of Viewport Class """
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def set_img(self, width, height):
        """
        STEP 5:
        create self.img_width and self.img_height
        """
        # Replace the following line:
        self.img_width = width
        self.img_height = height
        self.x = (self.img_width - self.width) // 2     # center image
        self.y = (self.img_height - self. height) // 2  # center image
        return self

    def move_up(self):
        """
        I've done this one for you.  Compare it to the
        move_up FUNCTION in img_viewer.py: it's very similar!

        Make similar changes in move_up, move_left, and move_right.
        """
        self.y -= self.height // 4
        top = self.y - self.height   # top is a local variable, not part of self
        if top < 0:
            self.y = self.height
        return self

    def move_down(self):
        """
        STEP 6:
        Copy move_down from img_viewer.py, and modify it
        to use self.x, self.y, self.width, self.height,
        self.img_width, and self.img_height.

        See move_up(self) method just above.
        """
        self.y += self.height // 4  
        if self.y > self.img_height:
            self.y = self.height - 1
        return self

    def move_left(self):
        """
        STEP 6:
        Copy move_left() function here, and adapt it.
        """
        self.x -= self.width // 4
        left = self.x - self.width  
        if left < 0:
            self.x = 0
        return self

    def move_right(self):
        """
        STEP 6:
        Copy move_right() function here, and adapt it.
        """
        self.x += self.width // 4
        if self.x > self.img_width:
            self.x = 0
        return self

    def display(self, img):
        """
        STEP 7:
        Copy display() function here, and adapt it.
        """
        top = self.y - self.height
        left = self.x - self.width
        bottom = self.y
        right = self.x

        for row in range(top, bottom):
            line = ''
            for pixel in img[row][left : right]:
                if pixel == '0':
                    line += '*'
                else:
                    line += '.'
            print (line)

        print ('x y w h:',self.x,self.y,self.width,self.height)
        return self

    def __str__(self):
        """
        Step 8:
        Implement __str__(self) method
        """
        return "Viewport (x y w h)({} {} {} {})".format(\
                    self.x,self.y,self.width,self.height)
