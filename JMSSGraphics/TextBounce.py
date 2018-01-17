from JMSSGraphics.JMSSGraphics_pyglet import *

import math

jmss = Graphics(200, 70)

name = "Apparition"
t = 0

@jmss.mainloop
def draw():
    global t
    t += 1
    jmss.clear(1, 1, 1)

    for i in range(len(name)):

        jmss.drawText(name[i], i * 18, 20 + 20.0 * ((i)/len(name)* 0.6+ 0.4) * math.cos(t/10.0 + (2.0* math.pi * i)/(len(name)-1)), fontName="Terminal",fontSize= 20,color = (0,0,0,1 - (i / (len(name)*1.2))))

jmss.run()