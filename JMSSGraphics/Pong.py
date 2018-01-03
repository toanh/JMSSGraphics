import random

import pyglet


class Game(pyglet.window.Window):
    def reset_ball(self):
        self.ball_sprite.x = 400
        self.ball_sprite.y = 300
        self.ball_sprite.vel_x = ((random.randint(0, 1) * 2) - 1) * 5
        self.ball_sprite.vel_y = ((random.randint(0, 1) * 2) - 1) * 5

    def __init__(self, fps, *args, **kwargs):
        super(Game, self).__init__(width=800,
                                   height=600,
                                   *args,
                                   **kwargs)

        player1_image = pyglet.resource.image("paddle.png")
        player2_image = pyglet.resource.image("paddle.png")
        ball_image = pyglet.resource.image("ball.png")

        self.player1_sprite = pyglet.sprite.Sprite(player1_image)
        self.player2_sprite = pyglet.sprite.Sprite(player2_image)
        self.ball_sprite = pyglet.sprite.Sprite(ball_image)

        self.player1_sprite.x = 50
        self.player1_sprite.y = self.height / 2
        self.player1_sprite.score = 0

        self.player2_sprite.x = self.width - 50 - self.player1_sprite.width
        self.player2_sprite.y = self.height / 2
        self.player2_sprite.score = 0

        self.reset_ball()

        self.keys = dict([(a, False) for a in range(255)])

        self.p1_score = pyglet.text.Label(str(self.player1_sprite.score),
                                          font_name='Terminal',
                                          font_size=36,
                                          x=150, y=self.height - 50,
                                          anchor_x='center', anchor_y='center')

        self.p2_score = pyglet.text.Label(str(self.player2_sprite.score),
                                          font_name='Terminal',
                                          font_size=36,
                                          x=self.width - 150, y=self.height - 50,
                                          anchor_x='center', anchor_y='center')

        pyglet.clock.schedule_interval(self.update, 1.0 / fps)
        pyglet.clock.set_fps_limit(fps)

    def draw(self):
        self.clear()
        self.p1_score.draw()
        self.p2_score.draw()
        self.player1_sprite.draw()
        self.player2_sprite.draw()
        self.ball_sprite.draw()

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True

    def on_key_release(self, symbol, modifiers):
        self.keys[symbol] = False

    def update(self, *args, **kwargs):

        if self.keys[pyglet.window.key.W]:
            self.player1_sprite.y += 5
        elif self.keys[pyglet.window.key.S]:
            self.player1_sprite.y -= 5
        if self.keys[pyglet.window.key.I]:
            self.player2_sprite.y += 5
        elif self.keys[pyglet.window.key.K]:
            self.player2_sprite.y -= 5

        if (self.player1_sprite.y < 0):
            self.player1_sprite.y = 0

        if (self.player1_sprite.y > self.height - self.player1_sprite.height):
            self.player1_sprite.y = self.height - self.player1_sprite.height

        if (self.player2_sprite.y < 0):
            self.player2_sprite.y = 0

        if (self.player2_sprite.y > self.height - self.player2_sprite.height):
            self.player2_sprite.y = self.height - self.player2_sprite.height

        if (self.ball_sprite.y > self.height - self.ball_sprite.height):
            self.ball_sprite.vel_y = - self.ball_sprite.vel_y

        if (self.ball_sprite.y < 0):
            self.ball_sprite.vel_y = - self.ball_sprite.vel_y

        if (self.ball_sprite.x + self.ball_sprite.width / 2 <= self.player1_sprite.x + self.player1_sprite.width and
                        self.ball_sprite.x + self.ball_sprite.width / 2 >= self.player1_sprite.x and
                        self.ball_sprite.y + self.ball_sprite.height / 2 >= self.player1_sprite.y and
                        self.ball_sprite.y + self.ball_sprite.height / 2 <= self.player1_sprite.y + self.player1_sprite.height):
            self.ball_sprite.vel_x = - self.ball_sprite.vel_x
            self.ball_sprite.x = self.player1_sprite.x + self.player1_sprite.width
            self.player1_sprite.score += 1

        if (self.ball_sprite.x + self.ball_sprite.width / 2 <= self.player2_sprite.x + self.player2_sprite.width and
                        self.ball_sprite.x + self.ball_sprite.width / 2 >= self.player2_sprite.x and
                        self.ball_sprite.y + self.ball_sprite.height / 2 >= self.player2_sprite.y and
                        self.ball_sprite.y + self.ball_sprite.height / 2 <= self.player2_sprite.y + self.player2_sprite.height):
            self.ball_sprite.vel_x = - self.ball_sprite.vel_x
            self.ball_sprite.x = self.player2_sprite.x - self.ball_sprite.width
            self.player2_sprite.score += 1

        if (self.ball_sprite.x < -self.ball_sprite.width or
                    self.ball_sprite.x > self.width):
            self.reset_ball()

        self.ball_sprite.x += self.ball_sprite.vel_x
        self.ball_sprite.y += self.ball_sprite.vel_y

        self.p1_score.text = str(self.player1_sprite.score)
        self.p2_score.text = str(self.player2_sprite.score)

        self.draw()


game = Game(60)
pyglet.app.run()