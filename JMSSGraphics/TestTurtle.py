from JMSSGraphics import *

import math

jmss = Graphics(width=600, height=400, title="My Game!", fps=60)

ball_ypos = 300
ball_yspeed = -2
ball_xpos = 0
ball_xspeed = 2


#bg_img = jmss.loadImage("Car2.png")

bg_img = jmss.loadImage("title.png")
#bg_img = jmss.loadImage("Frame1.png")
#ball_img = jmss.loadImage("Frame1.png")
ball_img = jmss.loadImage("water.png")

@jmss.mainloop
def game():
    global ball_ypos, ball_yspeed, ball_xpos, ball_xspeed

    if jmss.isKeyDown(KEY_W):
        ball_ypos += 10
    if jmss.isKeyDown(KEY_S):
        ball_ypos -= 10
    if jmss.isKeyDown(KEY_A):
        ball_xpos -= 10
    if jmss.isKeyDown(KEY_D):
        ball_xpos += 10

    jmss.clear()
    ball_ypos = ball_ypos + ball_yspeed
    ball_xpos = ball_xpos + ball_xspeed

    if ball_ypos < 0:
        ball_ypos = 0
        ball_yspeed = -ball_yspeed

    if ball_ypos > 400 - 16:
        ball_ypos = 400 - 16
        ball_yspeed = -ball_yspeed

    if ball_xpos < 0:
        ball_xpos = 0
        ball_xspeed = -ball_xspeed

    if ball_xpos > 600 - 16:
        ball_xpos = 600 - 16
        ball_xspeed = -ball_xspeed

    jmss.drawImage(bg_img, 0, 0, opacity=1)
    jmss.drawImage("Frame1.png", 0, 0, opacity=1)

    num_balls = 1000
    dim = math.sqrt(num_balls)
    jmss.drawLine(600, 400, 0, 0, 1, 1, 0, 1, 5)

    for i in range(num_balls):
        jmss.drawImage(ball_img, x=600 - ball_xpos - i //dim * 12, y=ball_ypos + i %dim * 12, \
                       rotation=600 - ball_xpos - i //dim * 12, anchorY=0.5, anchorX=0.5, opacity = 0.5)

    for i in range(100):
        jmss.drawRect(x1=ball_xpos, y1=100, x2=ball_xpos + 100, y2=110, r=0, g=1, b=0, a=1)
        jmss.drawCircle(ball_xpos, ball_ypos + i * 8, 4, 1, 0, 0, 0.5)
        jmss.drawRect(x1=ball_xpos + i * 8, y1=0, x2=ball_xpos + i * 8 + 2, y2=8, r=1, g=1, b=1, a=0.5)

    for i in range(100):
        jmss.drawPixel(x=ball_xpos + i * 8, y= i * 8, r= 1, g = 1, b = 0, a = 1)

    jmss.drawLine(0, 400, 600, 0, 1, 1, 0, 1, 5)
    jmss.drawLine(10, 400, 610, 0, 1, 0, 0, 0.5, 5)

    jmss.drawPixel(10, 300, 1, 1, 1, 1)

    jmss.drawText("hello, world!", 0, 0, fontSize=20, color=(1, 0, 0, 1))

    jmss.drawLine(600, 200, 0, 400, 0, 1, 0, 1, 5)
jmss.run()

