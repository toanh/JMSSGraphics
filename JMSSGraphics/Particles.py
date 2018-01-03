from JMSS import *
from vector import *

import turtle
import random
import math

particles = []

test = {'x': 10, 'y': 20}
print (test["x"])

spawnRate = 20
spawnTimer = spawnRate

numParticlesSpawn = 1

x = 0
y = 0
t = 0

def spawnParticle(t):
    c = 1.0#(math.sin(t * 0.1) / 2) + 0.50
    # print (c)
    particles.append({'x': -350,
                      'y': 100,
                      'velx': 20 * (random.random()),
                      'vely': 30 * (random.random() - 0.2),
                      'r': c,
                      'g': c,
                      'b': c,
                      'life': (random.random() * 2 + 0.5)})


def mainLoop():
    global x, y, spawnRate, spawnTimer, t

    jmss.clear()

    spawnTimer = spawnTimer - 1
    if (spawnTimer < 0):
        for i in range(0, numParticlesSpawn):
            spawnParticle(t)
        spawnTimer = spawnRate

    # update particles
    for particle in particles:
        # apply gravity
        particle["vely"] = particle["vely"] - 2
        particle["x"] = particle["x"] + particle["velx"]
        particle["y"] = particle["y"] + particle["vely"]

        if (particle["y"] < -210):
            particle["y"] = -210
            particle["vely"] = -0.8 * particle["vely"]

        if (particle["r"] <= 0):
            particles.remove(particle)
            continue

        particle["r"] = particle["r"] - 0.004
        if (particle["r"] < 0.0):
            particle["r"] = 0.0
        particle["g"] = particle["g"] - 0.004
        if (particle["g"] < 0.0):
            particle["g"] = 0.0
        particle["b"] = particle["b"] - 0.004
        if (particle["b"] < 0.0):
            particle["b"] = 0.0

    # draw particles
    for particle in particles:
        #jmss.drawRect((particle[4] * 255, particle[5] * 255, particle[6] * 255), (particle[0], particle[1], 10, 10))
        #jmss.drawCircle((particle["r"] * 255, particle["g"] * 255, particle["b"] * 255), (particle["x"], particle["y"]), 2)
        jmss.drawImage(image, (particle['x'], particle['y']), particle['r'] * 360, None, particle['r'] * 255, (64,64))

    t = t + 1

    jmss.drawImage(bld, (-390, 250), 0, None, 255, (64,550))

i = 0

def main():
    global i

    jmss.clear()
    i = i + 0.1
    jmss.drawRect((0, 255, 0), (0, 60, 60, 60), 2, i, (60, 120))
    jmss.drawRect((0, 255, 0), (0, 60, 60, 60), 2, i)


startx = -240
endx = -startx
starty = -240
endy = -starty
pixelsize = 1

def burningship(c_re, c_im):
    x = 0
    y = 0
    iteration = 0
    maxIterations = 20
    while (x * x + y * y <= 4 and iteration < maxIterations):
        x = abs(x)
        y = abs(y)
        x_new = x * x - y * y + c_re
        y = 2 * x * y + c_im
        x = x_new
        iteration = iteration + 1
    if (iteration < maxIterations):
        colour = (1.0 - iteration / maxIterations, 0, 0)
    else:
        colour = (0,0,0)
    return colour

def drawFractal():
    global startx, endx, starty, endy, pixelsize

    for y in range(starty, endy + 1):
        for x in range(startx, endx + 1):
            colour = burningship(x / (endx - startx) * 4, -y / (endy - starty) * 4)
            jmss.drawRect((colour[0] * 255, colour[1] * 255, colour[2] * 255),
                          (x * pixelsize, y * pixelsize, pixelsize, pixelsize))


population = []

def Infect(row, col, strand, pop):
    if strand in pop[row][col]['immunities']:
        return
    pop[row][col]['state'] = 3
    pop[row][col]['immunities'].append(strand)

def Recover(row, col, pop):
    pop[row][col]['state'] -= 1

def SetupPopulation():
    for i in range (0, 30):
        row = []
        for j in range (0, 30):
            row.append({'state':0,'immunities':[]})
        population.append(row)

    Infect(4, 4, 0, population)

import random
import copy

def InfectNeighbour(row, col, neighbour, strand, popcopy):
    nrow = row
    ncol = col
    if (neighbour == 0):
        nrow = row - 1
        ncol = col -1
    elif (neighbour == 1):
        nrow = row -1
    elif (neighbour == 2):
        nrow = row - 1
        ncol = col + 1
    elif (neighbour == 3):
        ncol = col - 1
    elif (neighbour == 4):
        ncol = col + 1
    elif (neighbour == 5):
        nrow = row + 1
        ncol = col - 1
    elif (neighbour == 6):
        nrow = row + 1
    elif (neighbour == 7):
        nrow = row + 1
        ncol = col + 1
    if (nrow < 0 or nrow >= len(population) or ncol < 0 or ncol >= len(population[0])):
        return
    # infect the neighbour
    #popcopy[nrow][ncol] = 3
    Infect(nrow, ncol, strand, popcopy)


def UpdatePopulation():
    global population
    popcopy = copy.deepcopy(population)
    for row in range (0, len(population)):
        for col in range (0, len(population[row])):
            state = population[row][col]['state']
            if (state != 0):
                # cell is infected...

                #  recover...
                Recover(row, col, popcopy)
                for strand in population[row][col]['immunities']:
                    # infect neighbours
                    neighbour = random.randint(0, 8)
                    InfectNeighbour(row, col, neighbour, strand, popcopy)
    population = copy.deepcopy(popcopy)

def DrawPopulation():
    cellsize = 10

    for row in range (0, len(population)):
        for col in range (0, len(population[row])):
            state = population[row][col]['state']
            color = (0, 255, 0)
            if (state == 0):
                color = (0, 0, 0)
            else:
                color = (state/3 * 255, 0, 0)

            jmss.drawRect(color, (col * (cellsize + 5)- 200, row * (cellsize + 5) - 200, cellsize, cellsize))

s = 0

def KeyListener(event):
    global s
    if (event.type == pygame.KEYUP and event.key == pygame.K_a):
        print(s)
        s = s + 1
        Infect(10, 10, s, population)
    if (event.type == pygame.MOUSEBUTTONUP):
        cellsize = 10
        pos = jmss.getMousePos()
        cellrow = int((pos[1] + 200) / (cellsize + 5))
        cellcol = int((pos[0] + 200) / (cellsize + 5))
        s = s + 1
        Infect(cellrow, cellcol, s, population)
        print (pos)

def InfectionSim():
    global s
    UpdatePopulation()
    DrawPopulation()

stars = []
blackholes = []


def SpawnGalaxyStarsByRing(center, numrings, color = (255, 255, 255)):
    for i in range(0, numrings):
        radius = 4 + i * 3
        circumference = radius * 2 * 3.14159
        for j in range (0, int(circumference / 5) + 1):
            a = j / radius * 5
            pos = Vector(radius * math.cos(a), radius * math.sin(a)) + center

            relpos = pos - center
            magnitude = math.sqrt(10 / relpos.norm())
            vel = Vector(relpos[1], -relpos[0])
            vel = vel.normalize()
            if (color[0] == 255):
                stars.append([pos,
                              magnitude * vel,
                              Vector(0,0),
                              [180 + 75 * (1 - i/numrings), 255, 255]])
            else:
                stars.append([pos,
                              magnitude * vel,
                              Vector(0,0),
                              [255, 255, 180 + 75 * (1 - i/numrings)]])

def SpawnGalaxyStars(center, numstars, radius, color = (255, 255, 255)):
    for i in range(0, numstars):
        d = random.random() * radius + 4
        a = random.random() * 3.14159 * 2

        pos = Vector(d * math.cos(a), d * math.sin(a)) + center

        relpos = pos - center
        magnitude = math.sqrt(10 / relpos.norm())
        vel = Vector(relpos[1], -relpos[0])
        vel = vel.normalize()
        if (color[0] == 255):
            stars.append([pos,
                          magnitude * vel,
                          Vector(0,0),
                          [180 + 75 * (1 - d/44), random.random() * 75 + 180, random.random() * 75 + 180]])
        else:
            stars.append([pos,
                          magnitude * vel,
                          Vector(0,0),
                          [random.random() * 75 + 180, random.random() * 75 + 180, 180 + 75 * (1 - d/44)]])

def Initialise():
    centre = Vector(-150, -80)
    blackholes.append([centre,     # position
                       Vector(0.08,0),     # velocity
                       Vector(0,0)      # acceleration
                       ])
    SpawnGalaxyStars(centre, 400, 40, (180, 180, 255))
    #SpawnGalaxyStarsByRing(centre, 20, (180, 180, 255))

    centre = Vector(150, 80)
    blackholes.append([centre,     # position
                       Vector(-0.08,0),     # velocity
                       Vector(0,0)      # acceleration
                       ])
    SpawnGalaxyStars(centre, 800, 80, (255, 180, 180))
    #SpawnGalaxyStarsByRing(centre, 20, (180, 180, 255))

def Render():
    jmss.clear()
    # draw the stars around the supermassive black holes
    for i in range(0, len(stars)):
        #jmss.drawCircle(stars[i][3], stars[i][0], 1)
        jmss.drawPixel(stars[i][0], stars[i][3])
    for i in range(0, len(blackholes)):
        jmss.drawCircle((255,255,255), blackholes[i][0],  5)


def UpdateStatic():
    # apply gravity from the black holes on the stars
    for j in range(0, 400):
        # apply gravity force
        difference = blackholes[0][0] - stars[j][0]

        direction = difference.normalize()
        distance = difference[0]*difference[0] + difference[1]*difference[1]

        magnitude = 1/distance * 10;

        stars[j][2] += magnitude * direction;
    for j in range(400, len(stars)):
        # apply gravity force
        difference = blackholes[1][0] - stars[j][0]

        direction = difference.normalize()
        distance = difference[0]*difference[0] + difference[1]*difference[1]

        magnitude = 1/distance * 10;

        stars[j][2] += magnitude * direction;


    # update the stars
    for i in range(0, len(stars)):
        # integrate
        stars[i][1] += stars[i][2]
        stars[i][0] += stars[i][1]

        # zero out the force
        stars[i][2] = Vector(0,0)

    return

def Update():

    for i in range(0, len(blackholes)):
        for j in range(1, len(blackholes)):
            if (i == j):
                continue
            # apply gravity force
            difference = blackholes[i][0] - blackholes[j][0]

            direction = difference.normalize()
            distance = difference[0]*difference[0] + difference[1]*difference[1]

            magnitude = 1/distance * 10;

            blackholes[j][2] += magnitude * direction;

            blackholes[i][2] -= magnitude * direction;

    # update the black holes
    for i in range(0, len(blackholes)):
        # integrate
        blackholes[i][1] += blackholes[i][2]
        blackholes[i][0] += blackholes[i][1]

        # zero out the force
        blackholes[i][2] = Vector(0,0)

    # apply gravity from the black holes on the stars
    for i in range(0, len(blackholes)):
        for j in range(0, len(stars)):
            # apply gravity force
            difference = blackholes[i][0] - stars[j][0]

            direction = difference.normalize()
            distance = difference[0]*difference[0] + difference[1]*difference[1]

            magnitude = 1/distance * 10;

            stars[j][2] += magnitude * direction;


    # update the stars
    for i in range(0, len(stars)):
        # integrate
        stars[i][1] += stars[i][2]
        stars[i][0] += stars[i][1]

        # zero out the force
        stars[i][2] = Vector(0,0)

    return

gravity = False

def Simulate():
    global gravity

    if (gravity):
        Update()
    else:
        UpdateStatic()
    Render()

def SimulationKeyListener(event):
    global gravity
    if (event.type == pygame.KEYUP and event.key == pygame.K_a):
        gravity = not gravity

offset = 0
y = 200
vel_y = 0

def TurtleTest():
    global offset, y, vel_y
    jmss.clear()

    t1.penUp()
    t1.setPos(0, 0)
    t1.setHeading(0)

    t1.penDown()
    for i in range(0, 36):
        j = (i + offset) % 36
        t1.setPenColor((j * 255/36, 0, 0))
        t1.forward(100)
        t1.turnLeft(120)
        t1.forward(100)
        t1.turnLeft(120)
        t1.forward(100)
        t1.turnLeft(120)
        t1.turnLeft(10)

    t2.penUp()
    t2.setPos(200, 100)
    t2.penDown()
    for i in range(0, 36):
        t2.beginFill()

        j = (i + offset) % 36
        t2.setPenColor((0, 255 - j * 255 / 36, 0))
        t2.setFillColor((0, j * 255 / 36, 0))
        t2.forward(50)
        t2.turnRight(120)
        t2.forward(50)
        t2.turnRight(120)
        t2.forward(50)
        t2.turnRight(120)
        t2.endFill()
        t2.turnRight(10)

    t3.penUp()
    t3.setPos(-200, -100)
    t3.penDown()
    for i in range(0, 36):
        t3.beginFill()

        j = (i + offset) % 36
        t3.setPenColor((j * 255/36, j * 255/36, j * 255/36))
        t3.setFillColor((j * 255 / 36, j * 255 / 36, j * 255 / 36))
        t3.forward(50)
        t3.turnRight(90)
        t3.forward(50)
        t3.turnRight(90)
        t3.forward(50)
        t3.turnRight(90)
        t3.forward(50)
        t3.turnRight(90)
        t3.endFill()
        t3.turnRight(10)
    offset = (offset + 1) % 36

    vel_y = vel_y - 1
    y = y + vel_y
    if (y < -200):
        y = -200
        vel_y = -vel_y

    jmss.drawCircle(((200 - y)/400 * 255 , 0, (200 - y)/400 * 255),(0, y), 30, 0)
    jmss.drawImage(image, (0 - 16,y + 16), 0, None, 255 - (200-y)/400 * 255, (32,32))



jmss = Graphics(800, 600, "Galaxies Simulation")
image = jmss.loadImage("smiley.png")
jmss.setFPS(60)
#Initialise()
#jmss.addEventListener(SimulationKeyListener)
#jmss.run(Simulate)
t1 = jmss.createTurtle()
t2 = jmss.createTurtle()
t3 = jmss.createTurtle()
jmss.run(TurtleTest)


'''
jmss = Graphics(800, 600, "Bouncing Ghosts")
#image = jmss.loadImage("smiley.png")
#image = jmss.loadImage("ghost.png")
#bld = jmss.loadImage("building.png")
#SetupPopulation()
#jmss.addEventListener(KeyListener)
#jmss.run(InfectionSim)
jmss.run(mainLoop)
#jmss.run(drawFractal)


'''