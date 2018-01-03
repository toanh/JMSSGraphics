import random

from JMSSGraphics.JMSSGraphics_pyglet import *

ball_sprite = None

player1_sprite = None
player2_sprite = None

p1_score = None
p2_score = None


def reset_ball():
    global ball_sprite
    ball_sprite.x = 400
    ball_sprite.y = 300
    ball_sprite.vel_x = ((random.randint(0, 1) * 2) - 1) * 5
    ball_sprite.vel_y = ((random.randint(0, 1) * 2) - 1) * 5

def init():
    global player1_sprite, player2_sprite, ball_sprite, p1_score, p2_score
    player1_sprite = jmss.createSprite("paddle.png")
    player2_sprite = jmss.createSprite("paddle.png")
    ball_sprite = jmss.createSprite("ball.png")

    player1_sprite.x = 50
    player1_sprite.y =300
    player1_sprite.score = 0

    player2_sprite.x = 800 - 50 - player1_sprite.width
    player2_sprite.y = 300
    player2_sprite.score = 0

    reset_ball()


    p1_score = jmss.createLabel(str(player1_sprite.score),
                                      fontName='Terminal',
                                      fontSize=36,
                                      x=150, y=600 - 50,
                                      anchorX='center', anchorY='center')

    p2_score = jmss.createLabel(str(player2_sprite.score),
                                      fontName='Terminal',
                                      fontSize=36,
                                      x=800 - 150, y=600 - 50,
                                      anchorX='center', anchorY='center')

def draw():
    global player1_sprite, player2_sprite, ball_sprite, p1_score, p2_score
    jmss.clear()
    p1_score.draw()
    p2_score.draw()
    player1_sprite.draw()
    player2_sprite.draw()
    ball_sprite.draw()


def update():
    global player1_sprite, player2_sprite, ball_sprite, p1_score, p2_score
    if jmss.isKeyDown(KEY_W):
        player1_sprite.y += 5
    elif jmss.isKeyDown(KEY_S):
        player1_sprite.y -= 5
    if jmss.isKeyDown(KEY_I):
        player2_sprite.y += 5
    elif jmss.isKeyDown(KEY_K):
        player2_sprite.y -= 5

    if (player1_sprite.y < 0):
        player1_sprite.y = 0

    if (player1_sprite.y > 600 - player1_sprite.height):
        player1_sprite.y = 600 - player1_sprite.height

    if (player2_sprite.y < 0):
        player2_sprite.y = 0

    if (player2_sprite.y > 600 - player2_sprite.height):
        player2_sprite.y = 600 - player2_sprite.height

    if (ball_sprite.y > 600 - ball_sprite.height):
        ball_sprite.vel_y = - ball_sprite.vel_y

    if (ball_sprite.y < 0):
        ball_sprite.vel_y = - ball_sprite.vel_y

    if (ball_sprite.x + ball_sprite.width / 2 <= player1_sprite.x + player1_sprite.width and
                    ball_sprite.x + ball_sprite.width / 2 >= player1_sprite.x and
                    ball_sprite.y + ball_sprite.height / 2 >= player1_sprite.y and
                    ball_sprite.y + ball_sprite.height / 2 <= player1_sprite.y + player1_sprite.height):
        ball_sprite.vel_x = - ball_sprite.vel_x
        ball_sprite.x = player1_sprite.x + player1_sprite.width
        player1_sprite.score += 1

    if (ball_sprite.x + ball_sprite.width / 2 <= player2_sprite.x + player2_sprite.width and
                    ball_sprite.x + ball_sprite.width / 2 >= player2_sprite.x and
                    ball_sprite.y + ball_sprite.height / 2 >= player2_sprite.y and
                    ball_sprite.y + ball_sprite.height / 2 <= player2_sprite.y + player2_sprite.height):
        ball_sprite.vel_x = - ball_sprite.vel_x
        ball_sprite.x = player2_sprite.x - ball_sprite.width
        player2_sprite.score += 1

    if (ball_sprite.x < -ball_sprite.width or
                ball_sprite.x > 800):
        reset_ball()

    ball_sprite.x += ball_sprite.vel_x
    ball_sprite.y += ball_sprite.vel_y

    p1_score.text = str(player1_sprite.score)
    p2_score.text = str(player2_sprite.score)

jmss = Graphics(800, 600)


@jmss.draw
def mainloop():
    update()
    draw()


init()
jmss.run()