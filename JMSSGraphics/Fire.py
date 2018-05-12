from JMSSGraphics import *
from Particle import *
import random
import math

jmss = Graphics(width = 800, height = 600, title = "Fire!", fps = 60)

images = []
images.append(jmss.loadImage("fire01.png"))
images.append(jmss.loadImage("fire02.png"))
images.append(jmss.loadImage("fire03.png"))
images.append(jmss.loadImage("fire04.png"))
images.append(jmss.loadImage("fire05.png"))

particles = []

def SpawnParticle(img, x, y, vel_x, vel_y, size, lifetime, rotation):
    new_particle = Particle()
    new_particle.img = img
    new_particle.x = x
    new_particle.y = y
    new_particle.vel_x = vel_x * 60
    new_particle.vel_y = vel_y * 60
    new_particle.height = size
    new_particle.width = size

    new_particle.orig_height = size
    new_particle.orig_width = size

    new_particle.lifetime = lifetime
    new_particle.life = lifetime

    new_particle.rotation = rotation

    particles.append(new_particle)

def UpdateParticles(dt):
    for p in particles:
        t = float(p.life) / p.lifetime

        p.life -= dt

        p.width = t * p.orig_width
        p.height = t * p.orig_height

        p.x += p.vel_x * dt
        p.y += p.vel_y * dt

    for p in particles:
        if p.x < -p.width or p.x > jmss.width:
            particles.remove(p)
            continue
        if p.y < -p.height or p.y > jmss.height:
            particles.remove(p)
            continue
        if p.life < 0:
            particles.remove(p)
            continue

def DrawParticles():
    for p in particles:
        jmss.drawImage(p.img, p.x - p.width/2, p.y, p.width, p.height, \
                       p.rotation, 0.5, 0.5, opacity= 0.5)

@jmss.mainloop
def Game(dt):
    for _ in range(5):
        fire_img = random.choice(images)
        size = fire_img.height + random.randint(-fire_img.height/6, fire_img.height/6)
        size /= 1.2
        rand_x = random.randint(-20, 20)
        max_lifetime = (1 - (abs(rand_x) / 20.0)) * 1.5

        x, y = jmss.getMousePos()

        SpawnParticle(fire_img,
                      x + rand_x, \
                      y + random.randint(-15, 15),\
                      0, \
                      random.random() * 5 + 1, \
                      size,
                      0.25 + random.random() * max_lifetime,
                      (random.random() * 3.14159265359 / 4) - 3.14159265359 / 8)

    jmss.set_blend_type(BLEND_ADDITIVE)
    jmss.clear(0, 0, 0, 1)

    UpdateParticles(dt)
    DrawParticles()
    jmss.drawText(str(len(particles)), 0, 0)


jmss.run()