"""
A configurable plotting package.
Reads data from a .csv file where each line has one x and one or more y values.
Also reads a configuration file.
Produces a 2D plot of the x,y values, and also saves them to a .ps file.

Author: Alejo Hausner (ah@cs.unh.edu) Sept. 2019.
"""

from tkinter import *
import sys
import datetime
import csv

class Display:
    """
    A Tk Canvas, with a rectangular drawing region inside it.
    """
    def __init__(self, master, w, h, margin, x_range, left_range, right_range):
        """Ctor.  Create the Canvas, and get the drawing region's params.

        Parameters
        ----------
        master: Tk
            contains this Canvas
        w: int
            width (in pixels) of the canvas
        h: int
            height (in pixels) of the canvas
        margin: int
            size of region, in the canvas, around the drawing region.
        x_range: tuple of number
            the min and max x values in the drawing region.
        left_range: tuple of number
            the min and max y values in the drawing region, for the left scale
        right_range: tuple of number
            the min and max y values in the drawing region, for the right scale
        """

        self.plot = Canvas(master, width = w, height = h)
        self.plot.pack()

        self.x_offset = margin
        self.x_scale = (w - 2 * margin) / range_length(x_range)
        self.x_min = x_range[0]

        self.left_offset = h - margin
        self.left_scale = -(h - 2 * margin) / range_length(left_range)
        self.left_min = left_range[0]

        self.right_offset = h - margin
        self.right_scale = -(h - 2 * margin) / range_length(right_range)
        self.right_min = right_range[0]

        self.x_left = margin
        self.x_right = w - margin
        self.y_bottom = h - margin
        self.y_top = margin

    def coords(self, x, y, side):
        """Transform a point onto the drawing region.

        Parameters
        ----------
        x, y: numbers
            the point
        side: str
            "left" or "right"
        """

        x = self.x_offset + self.x_scale * (x - self.x_min)
        if side == "left":
            y = self.left_offset + self.left_scale * (y - self.left_min)
        else:
            y = self.left_offset + self.right_scale * (y - self.right_min)
        # Check if point is in bounds
        if self.x_left <= x and x <= self.x_right and\
           self.y_top <= y and y <= self.y_bottom:
            return x, y
        else:
            return None, None

    def draw_shape(self, x, y, shape, color):
        """Draw a shape.

        Parameters
        ----------
        x, y : float
           center position of shape
        shape: str
           name of shape
        color: str
           color of shape
        """
        if shape == 'uptriangle':
            self.plot.create_polygon(((x-2, y+1), (x+2, y+1), (x,y-2)),
                                     fill=color)
        elif shape == 'downtriangle':
            self.plot.create_polygon(((x-2, y-1), (x+2, y-1), (x,y+2)),
                                     fill=color)

def read_data(filename):
    """Read a table from a .csv file.
    The first row of the table will have a header line,
    which names the columns.

    Parameter:
    ----------
    filename : str
        the name of the .csv file.
    """
    file = open(filename, 'r')
    data = []
    for i, line in enumerate(file):
        line = line.rstrip('\n\r')
        if i == 0:
            # Header, get column names
            headings = line.split(',')
        else:
            raw_fields = line.split(',')
            fields = []
            for field in raw_fields:
                field = to_num(field)
                fields.append(field)
            data.append(fields)
    file.close()
    return data, headings

def to_num(value):
    """Given a string, try to convert it to a float or int.
    If that fails, return the original string.

    Parameter
    ---------
    value : str
        the value being converted.
    """
    try:
        value = float(value)
        i = int(value)
        if value == i:
            value = i
    except ValueError:
        # Is it a date?
        if '/' in value:
            try:
                fields = value.split('/')
                if len(fields) == 2:
                    # Assume it's mm/dd
                    month, day = [to_num(field) for field in fields]
                    year = 2001
                else:
                    month, day, year = [to_num(field) for field in fields]
                value = datetime.date(year, month, day).toordinal()
            except ValueError:
                pass
        pass
    return value

def to_tuple_list(values):
    """Convert a list of strings into a list of tuples.

    Example:
       ["1,1", "2/14,Valentines", "123"]
    should yield
       [[1, 1], ['2/14', 'Valentines'], [123]]

    Parameter
    ---------
    values : list of str
        the list of strings.
    """
    tuples = []
    for value in values:
        raw_items = value.split(',')
        items = []
        for item in raw_items:
            item = to_num(item)
            items.append(item)
        tuples.append(items)
    return tuples

def to_dictionary(values):
    """Convert a list of strings into a dictionary

    Example:
        ["height:5", "width:50%", "123:apple"]
    should return
        {'height':5, 'width':'50%', 123:'apple'}

    Parameter
    ---------
    values : list of str
        the list in question
    """
    dictionary = dict()
    for value in values:
        fields = value.split(':')
        if len(fields) == 2:
            key, value = fields
        else:
            key = value = fields[0]
        key = to_num(key)
        value = to_num(value)
        dictionary[key] = value
    return dictionary

def configure(filename):
    """Read a configuration file.

    Parameter
    ---------
    filename : str
        the .csv configuration file
    """
    config = dict()

    # Default values, in case they don't appear in file
    config['left_title'] = ""
    config['right_title'] = ""
    config['x_title'] = ""
    config['title'] = ""
    config['x_range'] = (0, 10)
    config['left_range'] = (0, 10)
    config['right_range'] = (0, 10)
    config['x_tics'] = {0:0, 5:5, 10:10}
    config['left_tics'] = {0:0, 5:5, 10:10}
    config['right_tics'] = ()
    config['x_type'] = 'number'
    config['left_type'] = 'number'
    config['right_type'] = 'number'
    config['x_grid'] = True
    config['left_grid'] = True
    config['right_grid'] = True
    config['columns'] = (0,1)
    config[0] = {'side':'x'}
    config[1] = {'side':'left', 'color':'black', 'style:':'line'}

    # Now open the file, and read all its lines
    try:
        file = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:
        # No config file.  Use default settings.
        return config

    reader = csv.reader(file)
    columns = []
    for row in reader:
        key = row[0]
        raw_values = row[1:]
        while raw_values[-1] == "":
            raw_values.pop()

        # Depending on the key, the values will have different kinds of data
        if 'range' in key:
            values = to_tuple_list(raw_values)
            config[key] = values[0]
        elif 'tics' in key:
            config[key] = to_dictionary(raw_values)
        elif key == 'data':
            column_info = to_dictionary(raw_values)
            column = column_info['column']
            config[column] = column_info
            columns.append(column)
        else:
            config[key] = to_num(raw_values[0])
    config['columns'] = columns

    file.close()
    return config

def range_length(range):
    """Convert a range into a number.

    Parameter
    ---------
    range: list of two values
    """
    start, end = (to_num(x) for x in range)
    return end - start

def draw_plot_area(config, display):
    """Draw the rectangular plotting area, with tics, titles, and grid lines.

    Parameters
    ----------
    config: dict
        the configuration values
    display: Display
        the drawable region
    """

    # The box where data will be plotted.
    display.plot.create_rectangle(display.x_left, display.y_top,
                                  display.x_right, display.y_bottom, fill="")

    text_font = ('Helvetica', 10)

    # The tics and vertical gridlines from the bottom

    for x in config['x_tics']:
        label = config['x_tics'][x]
        x, y = display.coords(x, config['left_range'][0], 'left')
        display.plot.create_text(x, display.y_bottom + 6,
                                 text=label, anchor=N, font=text_font)
        if config['x_grid']:
            display.plot.create_line(x, display.y_bottom,
                                     x, display.y_top, fill='lightgrey')

    # tics and horizontal gridlines from the right
    for y in config['left_tics']:
        label = config['left_tics'][y]
        x, y = display.coords(config['x_range'][0], y, 'left')
        display.plot.create_text(x - 6, y,
                                 text=label, anchor=E, font=text_font)
        if config['left_grid']:
            display.plot.create_line(x, y, display.x_right, y, fill='lightgrey')

    # tics and horizontal gridlines from the left
    for y in config['right_tics']:
        label = config['right_tics'][y]
        x, y = display.coords(config['x_range'][1], y, 'right')
        display.plot.create_text(x + 6, y,
                                 text=label, anchor=W, font=text_font)
        if config['right_grid']:
            display.plot.create_line(x, y, display.x_right, y, fill='lightgrey')

    # title
    display.plot.create_text((display.x_left + display.x_right) / 2,
                             display.y_top - 5,
                             text=config['title'], anchor=S, font=text_font)
    # label on x axis
    display.plot.create_text((display.x_left + display.x_right) / 2,
                             display.y_bottom + 20,
                             text=config['x_title'], anchor=N, font=text_font)
    # label on left y axis
    # Can't turn the text, so make a column of letters (ugly, I know)
    label = "\n".join(config['left_title'])
    display.plot.create_text(display.x_left - 20,
                             (display.y_bottom + display.y_top) / 2,
                             text=label, anchor=E, font=text_font)
    # label on right y axis
    label = "\n".join(config['right_title'])
    display.plot.create_text(display.x_right + 15,
                             (display.y_bottom + display.y_top) / 2,
                             text=label, anchor=W, font=text_font)

def draw_data(display, data, column, x_column, config):
    """Plot one sequence of values.

    Parameters
    ----------
    display: Display
        will draw into its Canvas.
    column: int
        which column of the table has the y coords.
    x_column: int or None
        which column of the table has the x coords.  If None, will auto-generate
    config: dict
        the configuration values
    """
    # How many data points?
    n = len(data)
    x_data = []
    y_data = []
    if x_column is None:
        dx = (config['x_range'][1] - config['x_range'][0]) / n
    color = config[column]['color']
    for i in range(n):
        y_data.append(data[i][column])
        if x_column is None:
            x_data.append(i * dx)
        else:
            x_data.append(data[i][x_column])

    if 'line' in config[column]['style']:
        for i in range(n):
            x, y = display.coords(x_data[i], y_data[i], config[column]['side'])
            if i == 0:
                x_prev = x
                y_prev = y
                continue

            if x is None or x_prev is None:
                continue

            display.plot.create_line(x, y, x_prev, y_prev, fill=color)
            x_prev = x
            y_prev = y

    if 'point' in config[column]['style']:
        for i in range(n):
            x, y = display.coords(x_data[i], y_data[i], config[column]['side'])
            if x is None:
                continue
            display.draw_shape(x, y, config[column]['shape'], color)

    if config[column]['style'] == 'bar':
        for i in range(n):
            x, y = display.coords(x_data[i], y_data[i], config[column]['side'])
            if x is None:
                continue
            display.plot.create_line(x, y, x, display.y_bottom, fill=color)



def plot(data_filename, config_filename):
    data, headings = read_data(data_filename)
    config = configure(config_filename)
    master = Tk()
    display = Display(master, 1100, 800, 50,
                      config['x_range'], config['left_range'],
                      config['right_range'])
    draw_plot_area(config, display)
    x_column = None
    for column in config['columns']:
        if config[column]['side'] == 'x':
            x_column = column
            break

    for column in config['columns']:
        if config[column]['side'] != 'x':
            draw_data(display, data, column, x_column, config)

    display.plot.update()
    display.plot.postscript(file='plot-output.ps', rotate=True,
                            pageheight="8.5i", pagewidth="11i")

    mainloop()

def usage():
    """Complain that the user ran the program incorrectly."""
    sys.stderr.write('Usage:\n')
    sys.stderr.write('  python plot.py <data.csv> <config.csv>\n')
    sys.exit()

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit()

    data_filename = sys.argv[1]
    config_filename = sys.argv[2]

    plot(data_filename, config_filename)

if __name__ == '__main__':
    main()

