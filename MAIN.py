# Imports stuff
import pyglet
from pyglet.window import key
import RectangleCollision
import random

# Point variable
points = 0

# Window stuff
window = pyglet.window.Window(width=800,height=600,caption='GAME')
icon = pyglet.image.load('icon.ico')
window.set_icon(icon)

# Part of key stuff
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Player Object
class player():
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

# Variable to check if the "w,s,a,d" is pressed
keypressed = False

# Update stuff
@window.event
def update1(dt):
    # Movment stuff
    global keypressed
    if keys[key.A] and keypressed == False:
        player.posx -= 2
        keypressed = True
        keypressed = False
    if keys[key.D] and keypressed == False:
        player.posx += 2
        keypressed = True
        keypressed = False
    if keys[key.S] and keypressed == False:
        player.posy -= 2
        keypressed = True
        keypressed = False
    if keys[key.W] and keypressed == False:
        player.posy += 2
        keypressed = True
        keypressed = False

    # Collision stuff
    if RectangleCollision.collision.rectangle(player.posx,player.posy,point.posx,point.posy,32,32,32,32):
        point.posx = random.randint(32,750)
        point.posy = random.randint(32,550)
        global points
        points += 1
        LabelPoints.label = pyglet.text.Label('points:' + str(points), x=10,y=580)

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
    LabelPoints.label.draw()

# Window stuff
pyglet.app.run()
