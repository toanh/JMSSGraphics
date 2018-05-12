from JMSSGraphics import *
import random

# creating window
jmss = Graphics(width = 640, height = 640, title = "Image", fps = 60)

width = 640
quarter_width = int(width / 4)
height = 640

data = []

def FillColour(r, g, b):
    global data
    # clears the data
    data = []
    for y in range(height):
        for x in range(width):
            # note: there will be height * width * 3 values in the list
            data.append(r)    # red
            data.append(g)    # green
            data.append(b)    # blue
    

#creates random coloured pixels
def CreateRandom():
    global data
    # clears the data
    data = []
    for y in range(height):
        for x in range(width):
            # note: there will be height * width * 3 values in the list
            data.append(random.random())    # red
            data.append(random.random())    # green
            data.append(random.random())    # blue
            
            
# creates 4 vertical strips: red, green, blue, yellow
def CreateStripes():
    global data
    # clears the data
    data = []
    for y in range(height):
        
        # colour bottom 1/4 red
        for x in range(quarter_width):
            data.append(1.0)        # red
            data.append(0)          # green
            data.append(0)          # blue
            
        # colour second 1/4 green
        for x in range(quarter_width):
            data.append(0)          # red
            data.append(1.0)        # green
            data.append(0)          # blue

        # colour third 1/4 blue
        for x in range(quarter_width):
            data.append(0)          # red
            data.append(0)          # green
            data.append(1.0)        # blue

        # colour right 1/4 yellow
        for x in range(quarter_width):
            data.append(1.0)        # red
            data.append(1.0)        # green
            data.append(0)          # blue


@jmss.mainloop
def Draw():
    jmss.drawRawPixels(data, x = 0, y = 0, width = 640, height = 640)

CreateStripes()
#FillColour(1.0, 0, 1.0)
#CreateRandom()
    
jmss.run()


