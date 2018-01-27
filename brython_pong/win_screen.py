#Importing the JMSS graphics code
from JMSSGraphics_brython import *

#Creating the Graphics Object
jmss = Graphics(width = 600, height = 400, title = "My awesome game!", fps = 60)

#Declaring my variables
ball_xpos = 300
ball_ypos = 200
ball_xdir = -4
ball_ydir = -4

paddle1_xpos = 25
paddle1_ypos = 100

paddle2_xpos = 600 - 25 - 24
paddle2_ypos = 100

paddle1_lives = 3
paddle2_lives = 3

#declare out game_state variable
game_state = 0      # 0: title screen, 1: game, 2: win screen

#pre-load our images into RAM (memory)
ball_image = jmss.loadImage("baby.png")
paddle1_image = jmss.loadImage("paddle_red.png")
paddle2_image = jmss.loadImage("paddle_blue.png")
background_image = jmss.loadImage("background.png")
title_image = jmss.loadImage("title.png")

#pre-load our sound files
blip_sound = jmss.loadSound("blip.wav", streaming = False)
background_music = jmss.loadSound("just_dance.mp3", streaming = True)

jmss.playSound(background_music, loop = True)

#The main loop code is below, this gets run once per frame
@jmss.mainloop
def Game():
    global ball_xpos, ball_ypos, ball_xdir, ball_ydir, ball_image, paddle1_xpos, paddle1_ypos, \
           paddle1_image, paddle2_xpos, paddle2_ypos, paddle2_image, paddle1_lives, \
           paddle2_lives, game_state
    #code for the title screen:
    if game_state == 0:
        # checks to see if space is pressed, if so, change the game_state to the game
        if jmss.isKeyDown(KEY_SPACE):
            game_state = 1
        # draw the title screen
        jmss.drawImage(title_image, 0, 0)
    #code for the game
    elif game_state == 1:
        # first check if any of the players have lost
        if paddle1_lives <= 0 or paddle2_lives <= 0:
            # transition to the next win screen state
            game_state = 2
        else:
            #Code to update my game
            ball_xpos = ball_xpos + ball_xdir
            ball_ypos = ball_ypos + ball_ydir

            #checking for the bottom edge of the screen
            if ball_ypos <= 0:
                #snap it back to the botton
                ball_ypos = 0
                #flip its ydir
                ball_ydir = ball_ydir * -1

            #checking for the top edge of the screen
            if ball_ypos >= 400 - ball_image.height:
                #snap it back to the botton
                ball_ypos = 400 - ball_image.height
                #flip its ydir
                ball_ydir = ball_ydir * -1

            #checking for the ball going off the left hand side of the screen
            if ball_xpos <= -ball_image.width:
                #reset the position of the ball
                ball_xpos = 300
                ball_ypos = 200
                paddle1_lives -= 1      #same as paddle1_lives = paddle1_lives - 1
            #checking for the ball going off the right hand side of the screen
            if ball_xpos >= 600:
                #reset the position of the ball
                ball_xpos = 300
                ball_ypos = 200
                paddle2_lives -= 1

            #TODO: check for the ball going off the right hand side of the screen


            #Extension: increase the speed of the ball AFTER it has bounced
            #off each of the edges

            #checking for player keyboard input
            if jmss.isKeyDown(KEY_S):
                #move the paddle1 down
                paddle1_ypos = paddle1_ypos - 2
            if jmss.isKeyDown(KEY_W):
                #move the paddle1 up
                paddle1_ypos = paddle1_ypos + 2

            if jmss.isKeyDown(KEY_DOWN):
                #move the paddle1 down
                paddle2_ypos = paddle2_ypos - 2
            if jmss.isKeyDown(KEY_UP):
                #move the paddle1 up
                paddle2_ypos = paddle2_ypos + 2

            #TODO: introduce a second paddle on the other side of the screen
            #TODO: check for and restrict the movement of the paddles so that they do not
            #move off the screen

            #Extension: introduce momentum to the paddles


            #check for collision with the left hand paddle
            '''
            if xp >= x1
               and yp >= y1
               and xp <= x2
               and yp <= y2:
            '''
            if ball_xpos >= paddle1_xpos and ball_ypos >= paddle1_ypos and \
               ball_xpos <= paddle1_xpos + 24 and ball_ypos <= paddle1_ypos + 144:
                # the ball has collided with the left paddle
                ball_xpos = paddle1_xpos + 24   # snap the ball to the right edge of paddle
                                                # so that the ball does not appear 'inside' the paddle
                ball_xdir *= -1                 # abbreviation for ball_xdir = ball_xdir * -1
                jmss.playSound(blip_sound, loop = False)

            print(ball_image.width, ball_image.height)
            #check for collision with the right hand paddle
            if ball_xpos + ball_image.width >= paddle2_xpos and ball_ypos >= paddle2_ypos and \
               ball_xpos + ball_image.width <= paddle2_xpos + 24 and ball_ypos <= paddle2_ypos + 144:
                # the ball has collided with the left paddle
                ball_xpos = paddle2_xpos - ball_image.width   # snap the ball to the right edge of paddle
                                                # so that the ball does not appear 'inside' the paddle
                ball_xdir *= -1                 # abbreviation for ball_xdir = ball_xdir * -1
                jmss.playSound(blip_sound, loop = False)


            #TODO: do the collision for the right hand paddle
            #Note: use the bottom right hand corner of the ball instead of the anchor point

            #extension: give the player some more control over the bounced direction of the ball
            #e.g. if the ball hits the top or bottom edge of the paddle, have it bounce off at a more
            #extreme angle
            #or... use the direction that the paddle is moving, to induce some 'spin' or directionality
            #to the ball


            #Code to draw my game
            jmss.clear()
            jmss.drawImage(background_image, x = 0, y = 0)
            #the order of drawing means that the paddle is drawn first and
            #will be covered up by the ball if they overlap
            jmss.drawImage(paddle1_image, x = paddle1_xpos, y = paddle1_ypos)
            jmss.drawImage(paddle2_image, x = paddle2_xpos, y = paddle2_ypos)
            jmss.drawImage(ball_image, x = ball_xpos, y = ball_ypos)

            jmss.drawText("Lives: " + str(paddle1_lives), 10, 350, fontSize=20)
            jmss.drawText("Lives: " + str(paddle2_lives), 490, 350, fontSize=20)
        #
    # do the logic for the win screen
    elif game_state == 2:
        # check to see who our winner is
        if paddle1_lives <= 0:
            winner = 2
        else:
            winner = 1

        if jmss.isKeyDown(KEY_SPACE):
            game_state = 1
            ball_xpos = 300
            ball_ypos = 200
            ball_xdir = -4
            ball_ydir = -4

            paddle1_xpos = 25
            paddle1_ypos = 100

            paddle2_xpos = 600 - 25 - 24
            paddle2_ypos = 100

            paddle1_lives = 3
            paddle2_lives = 3

        # announce our winner
        jmss.clear()
        jmss.drawImage(background_image, x = 0, y = 0)
        jmss.drawText("Player " + str(winner) + " wins!!", 170, 200, fontSize = 30)

#This starts the Graphics object off and will run the main loop above
jmss.run()

jmss.pauseSound(background_music)




