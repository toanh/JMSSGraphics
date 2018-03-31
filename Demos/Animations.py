from JMSSGraphics import *


jmss = Graphics(800, 600, fps = 10)

animations = []
n = 1
while n <= 8:
    animations.append(jmss.loadImage("Aladdin0" + str(n) + ".png"))
    n += 1

@jmss.mainloop
def Game():
    global n, animations

    n += 1
    n %= len(animations)
    jmss.clear()
    jmss.drawImage(animations[n], 300, 200, width = 43 * 4, height = 61 * 4)



jmss.run()