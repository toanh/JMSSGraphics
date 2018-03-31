import pygame
import math

"""
A simple turtle class that uses PyGame. Implements instantaneous
rendering, ie. no animated drawing or turning
"""
class Turtle:
    """
    DO NOT instantiate directly. Always use the createTurtle() function
    in the Graphics class
    """
    def __init__(self, graphics):
        self.graphics = graphics

        self.pen_x = 0
        self.pen_y = 0
        self.pen_dx = 0
        self.pen_dy = 1
        self.pen_heading = 0
        self.pen_down = False
        self.pen_colour = (255, 255, 255)
        self.fill_colour = (255, 255, 255)
        self.fill_mode = False
        self.line_list = []
        self.pen_width = 1

    """
    Lifts the pen up. Disables drawing upon movement. Useful for
    repositioning the turtle.
        Arguments: None
        Returns:   None
    """
    def penUp(self):
        self.pen_down = False

    """
    Puts the pen back down on the screen. Turtle will now leave a 'trail'
    upon being moved.
        Arguments: None
        Returns:   None

    """
    def penDown(self):
        self.pen_down = True

    """
    Sets the pen color. This will colour the outline of any filled shapes too.
        Arguments:
            color - the colour of the pen. Color format is RGB: (255,255,255)
        Returns:   None

    """
    def setPenColor(self, color):
        self.pen_colour = color

    """
    Sets the fill color. This will colour the interior of any filled shapes.
        Arguments:
            color - the colour of the pen. Color format is RGB: (255,255,255)
        Returns:   None
    """
    def setFillColor(self, color):
        self.fill_colour = color

    """
    Sets the heading of the turtle in degrees. 
        Arguments:
            heading - the turtle's heading in degrees. 0 degrees is pointing in
            the positive y-axis (north)
        Returns:   None    
    """
    def setHeading(self, heading):
        self.pen_heading = heading
        angle = (90 - heading) * 3.14159265358979 / 180
        self.pen_dx = math.cos(angle)
        self.pen_dy = math.sin(angle)

    """
    Turns the turtle right by the number of the degrees.
        Arguments:
            angle - the number of degrees to turn right
        Returns:   None      
    """
    def turnRight(self, angle):
        self.setHeading(self.pen_heading + angle)

    """
    Turns the turtle left by the number of the degrees.
        Arguments:
            angle - the number of degrees to turn left
        Returns:   None      
    """
    def turnLeft(self, angle):
        self.setHeading(self.pen_heading - angle)

    """
    Sets the position of the turtle
        Arguments:
            x - the x coordinate
            y - the y coordinate
        Returns:   None      
    """
    def setPos(self, x, y):
        if (self.pen_down):
            pygame.draw.line(self.graphics.screen,
                             self.pen_colour,
                             self.graphics._conv((self.pen_x, self.pen_y)),
                             self.graphics._conv((x, y)),
                             self.pen_width)

        self.pen_x = x
        self.pen_y = y

    """
    Prepares the turtle to draw a filled in polygon.
    All the subsequent forward() and setPos() will form the outline of the polygon.
    Note that endFill() will need to be called to complete the shape and actually
    draw the polygon.
        Arguments: None
        Returns:   None      
    """
    def beginFill(self):
        self.line_list = []
        self.fill_mode = True

    """
    Completes the drawing of a filled in polygon.
    All the forward() and setPos() calls after the most recent beginFill() call
    will form the outline of the polygon.
        Arguments: None
        Returns:   None      
    """
    def endFill(self):
        self.fill_mode = False
        if (self.fill_colour == self.pen_colour):
            pygame.draw.polygon(self.graphics.screen,
                                self.pen_colour,
                                self.line_list,
                                0)
        else:
            pygame.draw.polygon(self.graphics.screen,
                                self.fill_colour,
                                self.line_list,
                                0)
            pygame.draw.polygon(self.graphics.screen,
                                self.pen_colour,
                                self.line_list,
                                self.pen_width)
        self.line_list = []

    """
    Moves the turtle forward by a set number of steps.
    Whether or not a line is drawn as a trail depends on whether the pen is down or up.
        Arguments:
            length - how far the turtle will move, in pixels.
        Returns:   None      
    """
    def forward(self, length):
        end_x = self.pen_dx * length + self.pen_x
        end_y = self.pen_dy * length + self.pen_y

        if (self.fill_mode):
            self.line_list.append(self.graphics._conv((end_x, end_y)))
        else:
            if (self.pen_down):
                pygame.draw.line(self.graphics.screen,
                                 self.pen_colour,
                                 self.graphics._conv((self.pen_x, self.pen_y)),
                                 self.graphics._conv((end_x, end_y)),
                                 self.pen_width)

        self.pen_x = end_x
        self.pen_y = end_y

"""
A simple graphics wrapper around PyGame.
It redefines the coordinate system to be like the Secondary School level cartesian axes.
It also exposes a simple turtle object that can be manipulated like the LOGO turtle for
basic line drawing.
"""
class Graphics:
    """
    Constructor:
        Arguments:
            width - the width of the window in pixels
            height - the height of the window in pixels
            title - the title to show in the window
            fps - how many frames per second to run the main update loop
        Returns:   None      
    """    
    def __init__(self, w, h, title = "", fps = 60):
        self.width = w
        self.height = h
        self.done = False
        self.fps = fps

        self.listeners = []

        # 0: turtle
        # 1: pygame
        self.renderer = 1

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    """
    Returns the PyGame screen canvas - for direct PyGame manipulation
        Arguments: None
        Returns:   None      
    """
    def getScreen(self):
        return self.screen

    """
    Sets the FPS (frames per second) for the update loop
        Arguments:
            fps - the number of frames per second
        Returns:   None      
    """
    def setFPS(self, fps):
        self.fps = fps

    """
    Creates a new turtle to draw basic line graphics
        Arguments: None
        Returns:
            A new turtle object (see definition at the top of this file)
    """
    def createTurtle(self):
        return Turtle(self)


    """
    Adds an event listener that will get triggered in the main loop based on received pygame events
    (e.g. keyboard or mouse events)
        Arguments:
            listener - An eventhandler function which takes a event as an argument
        Returns:
            None
    """
    def addEventListener(self, listener):
        self.listeners.append(listener)

    """
    The main update loop that gets run FPS times per second
        Arguments:
            mainloop - The main loop function with optional arguments
        Returns:
            None
    """
    def run(self, mainloop = None , *args):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
                    return
                for l in self.listeners:
                    l(event)

            if (mainloop is not None):
                if (len(args) > 0):
                    mainloop(args)
                else:
                    mainloop()

            c = pygame.time.Clock().tick(self.fps)
            pygame.display.flip()

    """
    The below functions perform conversions between coordinate spaces.
    These are not designed to be called externally.
    The _ prefix is used to denote internal functions.
    """
    def _conv(self, pt):
        return [int(self._conx(pt[0])), int(self._cony(pt[1]))]
    def _invconv(self, pt):
        return [int(self._invconx(pt[0])), int(self._invcony(pt[1]))]

    def _conx(self, x):
        return x + self.width /2
    def _invconx(self, x):
        return x - self.width/2

    def _cony(self, y):
        return self.height/2 - y
    def _invcony(self, y):
        return self.height/2 - y

    """
    Loads an image from disk and returns it as an object to be used in the drawImage() function
        Arguments:
            file - the filename of the image. Please include the extension.
        Returns:
            The image object
    """
    def loadImage(self, file):
        return pygame.image.load(file).convert_alpha()

    """
    Clears the screen with an optional colour.
        Arguments:
            color - (optional) the background colour. Color format is RGB: (255,255,255). Default is black.
        Returns:
            The image object
    """
    def clear(self, color = (0, 0, 0)):
        self.screen.fill(color)

    """
    Gets the current mouse position
        Arguments:
            None
        Returns:
            The mouse coordinates as a (x,y) tuple
    """
    def getMousePos(self):
        return self._invconv(pygame.mouse.get_pos())

    """
    Draws an image on the screen. The image must first be loaded in using loadImage().
        Arguments:
            image - the image object. (Obtained from loadImage())
            pos - a (x, y) tuple specifying the coordinates of the TOP LEFT HAND CORNER of the image.
            rotation - (optional) the angle of rotation to be applied to the image
            pivot - (optional) the pivot point of the rotation. Centre by default
            alpha - (optional) controls how transparent the image is. 0 is fully transparent. 255 is fully opaque.
            scale - (optional) a (width, height) tuple specifying how the image is to be stretches or squashed
            rect - (optional) a (x, y, width, height) rectangle specifying a sub-window of the original image to draw
                   (useful for spritesheets and animations etc.)            
        Returns:
            None
    """
    def drawImage(self, image, pos, rotation = 0, pivot = None, alpha = None, scale = None, rect = None):
        temp = image

        if (alpha is not None):
            temp = image.copy()
            temp.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

        if (scale is not None):
            temp = pygame.transform.scale(temp, scale)

        if (pivot is None):
            pivot = temp.get_rect().center
        temp = pygame.transform.rotate(temp, rotation)
        temp.get_rect().center = pivot

        self.screen.blit(temp, self._conv(pos), rect)

    """
    Draws a circle on the screen.
        Arguments:
            color - the circle's colour. Color format is RGB: (255,255,255)
            pos - a (x, y) tuple specifying the coordinates of the centre of the circle.
            radius - the radius of the circle in pixels
            width - the width of the outline of the circle. For a filled circle, set this to 0
        Returns:
            None
    """
    def drawCircle(self, color, pos, radius, width = 0):
        pygame.draw.circle(self.screen, color, self._conv(pos), radius, width)

    """
    Draws a pixel on the screen.
        Arguments:
            color - the pixel's colour. Color format is RGB: (255,255,255)
            pos - a (x, y) tuple specifying the coordinates of the pixel.
        Returns:
            None
    """
    def drawPixel(self, color, pos):
        self.screen.set_at(self._conv(pos), color)

    """
    Draws a rectangle on the screen.
        Arguments:
            color - the rectangle's colour. Color format is RGB: (255,255,255)
            rect - a (x, y, width, height) rectangle specifying the rectangle to draw on the screen             
            width - the width of the outline of the rectangle. For a filled rectangle, set this to 0
            rotation - (optional) the angle of rotation to be applied to the rectangle
            pivot - (optional) the pivot point of the rotation. This will be the top left hand corner by default.
        Returns:
            None
    """        
    def drawRect(self, color, rect, width = 0, rotation = 0, pivot = None):

        if (rotation != 0):
            points = []
            points.append([rect[0], rect[1]])
            points.append([rect[0] + rect[2], rect[1]])
            points.append([rect[0] + rect[2], rect[1] + rect[3]])
            points.append([rect[0], rect[1] + rect[3]])

            for point in points:
                if (pivot is None):
                    point[0] -= rect[0]
                    point[1] -= rect[1]
                else:
                    point[0] -= pivot[0]
                    point[1] -= pivot[1]

            rotated =[]
            for i in range(0, len(points)):
                rotatedPt = [0, 0]
                rotatedPt[0] = points[i][0] * math.cos(rotation) - points[i][1] * math.sin(rotation)
                rotatedPt[1] = points[i][0] * math.sin(rotation) + points[i][1] * math.cos(rotation)
                rotated.append(rotatedPt)

            for point in rotated:
                if (pivot is None):
                    point[0] += rect[0]
                    point[1] += rect[1]
                else:
                    point[0] += pivot[0]
                    point[1] += pivot[1]

                point[0] = self._conx(point[0])
                point[1] = self._cony(point[1])

            pygame.draw.polygon(self.screen, color, rotated, width)
        else:
            pygame.draw.rect(self.screen, color, pygame.Rect(self._conx(rect[0]), self._cony(rect[1]), rect[2], rect[3]), width)


##################################################################################################################################

"""
The MIT License (MIT)
Copyright (c) 2015 Mat Leonard
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

#import math

class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum(comp ** 2 for comp in self))

    def argument(self):
        """ Returns the argument of the vector, the angle clockwise from +y."""
        arg_in_rad = math.acos(Vector(0, 1) * self / self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0] < 0:
            return 360 - arg_in_deg
        else:
            return arg_in_deg

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    def rotate(self, *args):
        """ Rotate this vector. If passed a number, assumes this is a
            2D vector and rotates by the passed value in degrees.  Otherwise,
            assumes the passed value is a list acting as a matrix which rotates the vector.
        """
        if len(args) == 1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
            # So, if rotate is passed an int or a float...
            if len(self) != 2:
                raise ValueError("Rotation axis not defined for greater than 2D vector")
            return self._rotate2D(*args)
        elif len(args) == 1:
            matrix = args[0]
            if not all(len(row) == len(v) for row in matrix) or not len(matrix) == len(self):
                raise ValueError("Rotation matrix must be square and same dimensions as vector")
            return self.matrix_mult(matrix)

    def _rotate2D(self, theta):
        """ Rotate this vector by theta in degrees.

            Returns a new vector.
        """
        theta = math.radians(theta)
        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc * x - ds * y, ds * x + dc * y
        return Vector(x, y)

    def matrix_mult(self, matrix):
        """ Multiply this vector by a matrix.  Assuming matrix is a list of lists.

            Example:
            mat = [[1,2,3],[-1,0,1],[3,4,5]]
            Vector(1,2,3).matrix_mult(mat) ->  (14, 2, 26)

        """
        if not all(len(row) == len(self) for row in matrix):
            raise ValueError('Matrix must match vector dimensions')

            # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row) * self for row in matrix)

        return Vector(*product)

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector
        """
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return Vector(*product)

    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)

    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple(a / other for a in self)
            return Vector(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)
