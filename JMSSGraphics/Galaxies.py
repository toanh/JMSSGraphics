from JMSS import *

import random
import math
from vector import *

stars = []
blackholes = []

def Initialise():
    blackholes.append([Vector(0,0),     # position
                       Vector(0,0),     # velocity
                       Vector(0,0)      # acceleration
                       ])

    for i in range(0, 1):
        stars.append([Vector(0,20),
                      Vector(0,10),
                      Vector(0,0)])

def Render():
    # draw the stars around the supermassive black holes
    for i in range(0, len(stars)):
        jmss.drawCircle((1,1,1), stars[i][0], 5)


def Update():
    # apply gravity from the black holes on the stars
    # update the black holes


    # update the stars
    return

def Simulate():
    Update()
    Render()

jmss = Graphics(800, 600, "My first window")
jmss.run(Simulate)

