# Imports stuff
import pyglet
from pyglet.window import key
import RectangleCollision
import random

# Point variable
points = 0

# Window stuff
window = pyglet.window.Window(width=800,height=600,caption='GAME')
icon = pyglet.image.load('icon.png')
window.set_icon(icon)

# Part of key stuff
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Player Object
class player():
    direction = ''
    posx = 400
    posy = 300
    image = pyglet.image.load('player.png')

# Point object
class point():
    posx = random.randint(32,750)
    posy = random.randint(32,550)
    image = pyglet.image.load('point.png')

# Label for points object
class LabelPoints():
    label = pyglet.text.Label('points:' + str(points), x=10,y=580)
# Block1 objects
class block1():
    posx1 = 500
    posy1 = 100
    posx2 = 50
    posy2 = 500
    image = pyglet.image.load('block1.png')
# Solid object
class solid():
    def solid(obj1x,obj1y,obj2x,obj2y,obj1w=32,ob1h=32,obj2w=32,obj2h=32):
        if RectangleCollision.collision.rectangle(point.posx,point.posy,obj2x,obj2y,32,32,obj2w,obj2h):
            point.posx = random.randint(32,750)
            point.posy = random.randint(32,550)
        if RectangleCollision.collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w,ob1h,obj2w,obj2h):
            if player.direction == 'left': player.posx += 2
            if player.direction == 'right': player.posx -= 2
            if player.direction == 'down': player.posy += 2
            if player.direction == 'up': player.posy -= 2
            if player.direction == 'up/left':
                player.posx += 2
                player.posy -= 2
            if player.direction == 'up/right':
                player.posx -= 2
                player.posy -= 2
            if player.direction == 'down/left':
                player.posx += 2
                player.posy += 2
            if player.direction == 'down/right':
                player.posx -= 2
                player.posy += 2

# Update stuff
def update1(dt):
    # Movment stuff
    global keypressed
    if keys[key.A]:
        player.posx -= 2
        player.direction = 'left'
    if keys[key.D]:
        player.posx += 2
        player.direction = 'right'
    if keys[key.S] :
        player.posy -= 2
        player.direction = 'down'
    if keys[key.W]:
        player.posy += 2
        player.direction = 'up'
    if keys[key.W] and keys[key.A]:
        player.direction = 'up/left'
    if keys[key.W] and keys[key.D]:
        player.direction = 'up/right'
    if keys[key.S] and keys[key.A]:
        player.direction = 'down/left'
    if keys[key.S] and keys[key.D]:
        player.direction = 'down/right'
    # Collision stuff
    if RectangleCollision.collision.rectangle(player.posx,player.posy,point.posx,point.posy,32,32,32,32):
        point.posx = random.randint(32,750)
        point.posy = random.randint(32,550)
        global points
        points += 1
        LabelPoints.label = pyglet.text.Label('points:' + str(points), x=10,y=580)
    #  Make block1 solid
    solid.solid(player.posx,player.posy,block1.posx1,block1.posy1,32,32,128,32)
    solid.solid(player.posx,player.posy,block1.posx2,block1.posy2,32,32,128,32)

    # So you can leave the screen stuff
    if player.posx >= 770:
        player.posx -= 2
    if player.posx <= -1:
        player.posx += 2
    if player.posy >= 570:
        player.posy -= 2
    if player.posy <= -1:
        player.posy += 2

# Part of update stuff
pyglet.clock.schedule_interval(update1, 1/120)

# On draw stuff
@window.event
def on_draw():
    # Clears the window
    window.clear()
    # Draws the stuff on
    player.image.blit(player.posx,player.posy)
    point.image.blit(point.posx,point.posy)
    block1.image.blit(block1.posx1,block1.posy1)
    block1.image.blit(block1.posx2,block1.posy2)
    LabelPoints.label.draw()

# Window stuff
pyglet.app.run()
