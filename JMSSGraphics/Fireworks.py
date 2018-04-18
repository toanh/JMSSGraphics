from JMSSGraphics import *

jmss = Graphics(width=600, height=400, title="My Game!", fps=60)

ball_ypos = 300
ball_yspeed = -2
ball_xpos = 0
ball_xspeed = 2

ball_img = jmss.loadImage("water.png")

'''
loops

print hello, world 5 times
what if you want to print hello, world 100 times?

or ask the user how many times to repeat hello world?

draw 50 balls

======
lists
list of integers etc.
list of names
list of scores
list of text lines that scroll up the page

ask the user to enter in a list of what??
when the user clicks on the screen, draw a new ball there...
'''

@jmss.mainloop
def game():
    global ball_ypos, ball_yspeed, ball_xpos, ball_xspeed

    jmss.clear()

    i = 0
    while i < 20:
        jmss.drawImage(ball_img, x = ball_xpos + i * 30, y = ball_ypos)
        i += 1


jmss.run()

