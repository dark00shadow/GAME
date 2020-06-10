import pyglet
from pyglet.window import key
import RectangleCollision
import random

points = 0

window = pyglet.window.Window(width=800,height=600,caption='GAME')
icon = pyglet.image.load('icon.ico')
window.set_icon(icon)
keys = key.KeyStateHandler()
window.push_handlers(keys)

class player():
    posx = 400
    posy = 300
    image = pyglet.image.load('player.png')
class point():
    posx = random.randint(32,750)
    posy = random.randint(32,550)
    image = pyglet.image.load('point.png')
class LabelPoints():
    label = pyglet.text.Label('points:' + str(points), x=10,y=580)


@window.event
def update1(dt):
    if keys[key.A]:
        player.posx -= 2
    elif keys[key.D]:
        player.posx += 2
    elif keys[key.S]:
        player.posy -= 2
    elif keys[key.W]:
        player.posy += 2
    if RectangleCollision.collision.rectangle(player.posx,player.posy,point.posx,point.posy,32,32,32,32):
        point.posx = random.randint(32,750)
        point.posy = random.randint(32,550)
        global points
        points += 1
        LabelPoints.label = pyglet.text.Label('points:' + str(points), x=10,y=580)
    if player.posx >= 770:
        player.posx -= 2
    if player.posx <= -1:
        player.posx += 2
    if player.posy >= 570:
        player.posy -= 2
    if player.posy <= -1:
        player.posy += 2



pyglet.clock.schedule_interval(update1, 1/120)


@window.event
def on_draw():
    window.clear()
    player.image.blit(player.posx,player.posy)
    point.image.blit(point.posx,point.posy)
    LabelPoints.label.draw()
pyglet.app.run()