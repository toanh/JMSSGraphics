import pyglet
import math

# Key symbol constants

# ASCII commands
KEY_BACKSPACE     = 0xff08
KEY_TAB           = 0xff09
KEY_LINEFEED      = 0xff0a
KEY_CLEAR         = 0xff0b
KEY_RETURN        = 0xff0d
KEY_ENTER         = 0xff0d      # synonym
KEY_PAUSE         = 0xff13
KEY_SCROLLLOCK    = 0xff14
KEY_SYSREQ        = 0xff15
KEY_ESCAPE        = 0xff1b
KEY_KEY_SPACE         = 0xff20

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_LEFT          = 0xff51
KEY_UP            = 0xff52
KEY_RIGHT         = 0xff53
KEY_DOWN          = 0xff54
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58

# Misc functions
KEY_DELETE        = 0xffff
KEY_SELECT        = 0xff60
KEY_PRINT         = 0xff61
KEY_EXECUTE       = 0xff62
KEY_INSERT        = 0xff63
KEY_UNDO          = 0xff65
KEY_REDO          = 0xff66
KEY_MENU          = 0xff67
KEY_FIND          = 0xff68
KEY_CANCEL        = 0xff69
KEY_HELP          = 0xff6a
KEY_BREAK         = 0xff6b
KEY_MODESWITCH    = 0xff7e
KEY_SCRIPTSWITCH  = 0xff7e
KEY_FUNCTION      = 0xffd2

# Text motion constants: these are allowed to clash with key constants
KEY_MOTION_UP                = KEY_UP
KEY_MOTION_RIGHT             = KEY_RIGHT
KEY_MOTION_DOWN              = KEY_DOWN
KEY_MOTION_LEFT              = KEY_LEFT
KEY_MOTION_NEXT_WORD         = 1
KEY_MOTION_PREVIOUS_WORD     = 2
KEY_MOTION_BEGINNING_OF_LINE = 3
KEY_MOTION_END_OF_LINE       = 4
KEY_MOTION_NEXT_PAGE         = KEY_PAGEDOWN
KEY_MOTION_PREVIOUS_PAGE     = KEY_PAGEUP
KEY_MOTION_BEGINNING_OF_FILE = 5
KEY_MOTION_END_OF_FILE       = 6
KEY_MOTION_BACKSPACE         = KEY_BACKSPACE
KEY_MOTION_DELETE            = KEY_DELETE

# Number pad
KEY_NUMLOCK       = 0xff7f
KEY_NUM_SPACE     = 0xff80
KEY_NUM_TAB       = 0xff89
KEY_NUM_ENTER     = 0xff8d
KEY_NUM_F1        = 0xff91
KEY_NUM_F2        = 0xff92
KEY_NUM_F3        = 0xff93
KEY_NUM_F4        = 0xff94
KEY_NUM_HOME      = 0xff95
KEY_NUM_LEFT      = 0xff96
KEY_NUM_UP        = 0xff97
KEY_NUM_RIGHT     = 0xff98
KEY_NUM_DOWN      = 0xff99
KEY_NUM_PRIOR     = 0xff9a
KEY_NUM_PAGE_UP   = 0xff9a
KEY_NUM_NEXT      = 0xff9b
KEY_NUM_PAGE_DOWN = 0xff9b
KEY_NUM_END       = 0xff9c
KEY_NUM_BEGIN     = 0xff9d
KEY_NUM_INSERT    = 0xff9e
KEY_NUM_DELETE    = 0xff9f
KEY_NUM_EQUAL     = 0xffbd
KEY_NUM_MULTIPLY  = 0xffaa
KEY_NUM_ADD       = 0xffab
KEY_NUM_SEPARATOR = 0xffac
KEY_NUM_SUBTRACT  = 0xffad
KEY_NUM_DECIMAL   = 0xffae
KEY_NUM_DIVIDE    = 0xffaf

KEY_NUM_0         = 0xffb0
KEY_NUM_1         = 0xffb1
KEY_NUM_2         = 0xffb2
KEY_NUM_3         = 0xffb3
KEY_NUM_4         = 0xffb4
KEY_NUM_5         = 0xffb5
KEY_NUM_6         = 0xffb6
KEY_NUM_7         = 0xffb7
KEY_NUM_8         = 0xffb8
KEY_NUM_9         = 0xffb9

# Function keys
KEY_F1            = 0xffbe
KEY_F2            = 0xffbf
KEY_F3            = 0xffc0
KEY_F4            = 0xffc1
KEY_F5            = 0xffc2
KEY_F6            = 0xffc3
KEY_F7            = 0xffc4
KEY_F8            = 0xffc5
KEY_F9            = 0xffc6
KEY_F10           = 0xffc7
KEY_F11           = 0xffc8
KEY_F12           = 0xffc9
KEY_F13           = 0xffca
KEY_F14           = 0xffcb
KEY_F15           = 0xffcc
KEY_F16           = 0xffcd
KEY_F17           = 0xffce
KEY_F18           = 0xffcf
KEY_F19           = 0xffd0
KEY_F20           = 0xffd1

# Modifiers
KEY_LSHIFT        = 0xffe1
KEY_RSHIFT        = 0xffe2
KEY_LCTRL         = 0xffe3
KEY_RCTRL         = 0xffe4
KEY_CAPSLOCK      = 0xffe5
KEY_LMETA         = 0xffe7
KEY_RMETA         = 0xffe8
KEY_LALT          = 0xffe9
KEY_RALT          = 0xffea
KEY_LWINDOWS      = 0xffeb
KEY_RWINDOWS      = 0xffec
KEY_LCOMMAND      = 0xffed
KEY_RCOMMAND      = 0xffee
KEY_LOPTION       = 0xffef
KEY_ROPTION       = 0xfff0

# Latin-1
KEY_SPACE         = 0x020
KEY_EXCLAMATION   = 0x021
KEY_DOUBLEQUOTE   = 0x022
KEY_HASH          = 0x023
KEY_POUND         = 0x023  # synonym
KEY_DOLLAR        = 0x024
KEY_PERCENT       = 0x025
KEY_AMPERSAND     = 0x026
KEY_APOSTROPHE    = 0x027
KEY_PARENLEFT     = 0x028
KEY_PARENRIGHT    = 0x029
KEY_ASTERISK      = 0x02a
KEY_PLUS          = 0x02b
KEY_COMMA         = 0x02c
KEY_MINUS         = 0x02d
KEY_PERIOD        = 0x02e
KEY_SLASH         = 0x02f
KEY__0            = 0x030
KEY__1            = 0x031
KEY__2            = 0x032
KEY__3            = 0x033
KEY__4            = 0x034
KEY__5            = 0x035
KEY__6            = 0x036
KEY__7            = 0x037
KEY__8            = 0x038
KEY__9            = 0x039
KEY_COLON         = 0x03a
KEY_SEMICOLON     = 0x03b
KEY_LESS          = 0x03c
KEY_EQUAL         = 0x03d
KEY_GREATER       = 0x03e
KEY_QUESTION      = 0x03f
KEY_AT            = 0x040
KEY_BRACKETLEFT   = 0x05b
KEY_BACKSLASH     = 0x05c
KEY_BRACKETRIGHT  = 0x05d
KEY_ASCIICIRCUM   = 0x05e
KEY_UNDERSCORE    = 0x05f
KEY_GRAVE         = 0x060
KEY_QUOTELEFT     = 0x060
KEY_A             = 0x061
KEY_B             = 0x062
KEY_C             = 0x063
KEY_D             = 0x064
KEY_E             = 0x065
KEY_F             = 0x066
KEY_G             = 0x067
KEY_H             = 0x068
KEY_I             = 0x069
KEY_J             = 0x06a
KEY_K             = 0x06b
KEY_L             = 0x06c
KEY_M             = 0x06d
KEY_N             = 0x06e
KEY_O             = 0x06f
KEY_P             = 0x070
KEY_Q             = 0x071
KEY_R             = 0x072
KEY_S             = 0x073
KEY_T             = 0x074
KEY_U             = 0x075
KEY_V             = 0x076
KEY_W             = 0x077
KEY_X             = 0x078
KEY_Y             = 0x079
KEY_Z             = 0x07a
KEY_BRACELEFT     = 0x07b
KEY_BAR           = 0x07c
KEY_BRACERIGHT    = 0x07d
KEY_ASCIITILDE    = 0x07e


class JMSSPygletApp(pyglet.window.Window):
    def __init__(self, fps, graphics, *args, **kwargs):
        super(JMSSPygletApp, self).__init__(width=graphics.width,
                                   height=graphics.height, caption=graphics.title,
                                   *args,
                                   **kwargs)

        self.keys = dict([(a, False) for a in range(255)])

        self.graphics = graphics
        self.draw_func = None
        self.init_func = None

        pyglet.gl.glClearColor(0.5, 0, 0, 1)
        self.fps = fps

    def start(self):
        if (self.init_func is not None):
            self.init_func()
        pyglet.clock.schedule_interval(self.mainloop, 1.0 / self.fps)
        pyglet.clock.set_fps_limit(self.fps)

    def mainloop(self, *args, **kwargs):
        #self.graphics.update()
        if (self.draw_func is not None):
            self.draw_func()

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True

    def on_key_release(self, symbol, modifiers):
        self.keys[symbol] = False


class Graphics:
    def __init__(self, width, height, title = "", fps = 60):
        self.width = width
        self.height = height
        self.title = title
        self.done = False
        self.fps = fps

        self.listeners = []

        self.draw_func = None
        self.update_func = None

        self.app = JMSSPygletApp(fps, self)

        self.soundPlayers = {}

    def run(self):
        self.app.start()
        pyglet.app.run()

    def init(self, func):
        self.app.init_func = func

    def mainloop(self, func):
        self.app.draw_func = func

    def clear(self, r = 0, g = 0, b = 0, a = 1):
        pyglet.gl.glClearColor(r, g, b, a)
        self.app.clear()

    def setFPS(self, fps):
        self.fps = fps

    def loadImage(self, file):
        return pyglet.resource.image(file)

    def createSprite(self, image):
        # if the filename is supplied, create an image and autocreate the sprite
        if (isinstance(image, str)):
            return pyglet.sprite.Sprite(self.loadImage(image))
        else:
            return pyglet.sprite.Sprite(image)

    def isKeyDown(self, key):
        return self.app.keys[key]

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))

    def createLabel(self, text, fontName, fontSize, x, y, anchorX, anchorY):
        return pyglet.text.Label(text, font_name=fontName, font_size=fontSize, x = x, y = y, anchor_x = anchorX, anchor_y = anchorY)

    def loadSound(self, filename, streaming = False):
        return pyglet.media.load(filename=filename, streaming=streaming)

    def playSound(self, sound, loop = False):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()
            self.soundPlayers[sound] = None
        player = pyglet.media.Player()
        sg = pyglet.media.SourceGroup(sound.audio_format, None)
        sg.queue(sound)
        sg.loop = loop
        self.soundPlayers[sound] = player
        player.queue(sg)
        player.play()

    def pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, color = (1, 1, 1, 1), anchorX = "left", anchorY ="bottom"):
        label = pyglet.text.Label(text, color = self._convColor(color), font_name=fontName, font_size=fontSize, x = x, y = y, anchor_x = anchorX, anchor_y = anchorY)
        label.draw()

    def drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, rect=None):
        if (isinstance(image, str)):
            image = self.loadImage(image)
            sprite = pyglet.sprite.Sprite(image)
        else:
            sprite = pyglet.sprite.Sprite(image)

        if width is not None:
            sprite.scale_x =  width * 1.0 / sprite.width
        if height is not None:
            sprite.scale_y = height * 1.0  / sprite.height

        anchor_x = image.anchor_x
        anchor_y = image.anchor_y

        dx = 0
        dy = 0

        if anchorX is not None:
            dx = anchorX * image.width * sprite.scale_x
            image.anchor_x = anchorX * image.width


        if anchorY is not None:
            dy = anchorY * image.height * sprite.scale_y
            image.anchor_y = anchorY * image.height

        sprite.x = x + dx
        sprite.y = y + dy

        if opacity is not None:
            sprite.opacity = int(opacity * 255)

        sprite.rotation = rotation
        sprite.draw()

        image.anchor_x = anchor_x
        image.anchor_y = anchor_y

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


