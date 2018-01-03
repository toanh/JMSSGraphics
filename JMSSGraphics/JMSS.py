import pygame
import math

class Turtle:
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

    def penUp(self):
        self.pen_down = False

    def penDown(self):
        self.pen_down = True

    def setPenColor(self, color):
        self.pen_colour = color

    def setFillColor(self, color):
        self.fill_colour = color

    def setHeading(self, heading):
        self.pen_heading = heading
        angle = (90 - heading) * 3.1415926535 / 180
        self.pen_dx = math.cos(angle)
        self.pen_dy = math.sin(angle)

    def turnRight(self, angle):
        self.setHeading(self.pen_heading + angle)

    def turnLeft(self, angle):
        self.setHeading(self.pen_heading - angle)

    def setPos(self, x, y):
        if (self.pen_down):
            pygame.draw.line(self.graphics.screen,
                             self.pen_colour,
                             self.graphics._conv((self.pen_x, self.pen_y)),
                             self.graphics._conv((x, y)),
                             self.pen_width)

        self.pen_x = x
        self.pen_y = y

    def beginFill(self):
        self.line_list = []
        self.fill_mode = True

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


class Graphics:
    def __init__(self, w, h, title = "", fps = 60):
        self.width = w
        self.height = h
        self.done = False
        self.fps = fps

        self.listeners = []

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    def setFPS(self, fps):
        self.fps = fps

    def createTurtle(self):
        return Turtle(self)

    def addEventListener(self, listener):
        self.listeners.append(listener)

    def run(self, mainloop = None , *args):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                for l in self.listeners:
                    l(event)

            if (mainloop is not None):
                if (len(args) > 0):
                    mainloop(args)
                else:
                    mainloop()

            c = pygame.time.Clock().tick(self.fps)
            pygame.display.flip()

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

    def loadImage(self, file):
        return pygame.image.load(file).convert_alpha()

    def clear(self, color = (0, 0, 0)):
        self.screen.fill(color)

    def getMousePos(self):
        return self._invconv(pygame.mouse.get_pos())

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

    def drawCircle(self, color, pos, radius, width = 0):
        pygame.draw.circle(self.screen, color, self._conv(pos), radius, width)

    def drawPixel(self, pos, color):
        self.screen.set_at(self._conv(pos), color)

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


