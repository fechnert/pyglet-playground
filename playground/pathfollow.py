import time
import pyglet
import random

from utils.shapes import line, bezier, circle


window = pyglet.window.Window(
    width=800,
    height=400,
    caption='Python Paths',
)
window.clear()

PATH = line((200, 100), (600, 100))
PATH += bezier([(600, 100), (700, 100), (700, 200)])
PATH += bezier([(700, 200), (700, 300), (600, 300)])

#PATH += line((600, 300), (200, 300))
PATH += bezier([(600, 300), (500, 300), (500, 250), (400, 250)])
PATH += bezier([(400, 250), (300, 250), (300, 300), (200, 300)])

PATH += bezier([(200, 300), (100, 300), (100, 200)])
PATH += bezier([(100, 200), (100, 100), (200, 100)])
POS = 0


@window.event
def on_draw():

    global PATH
    window.clear()
    batch = pyglet.graphics.Batch()

    for point in PATH:
        batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', point), ('c3B', (96, 96, 96)))

    batch.draw()

    circle(PATH[int(POS)]).draw(pyglet.gl.GL_LINE_LOOP)


def update(dt):
    global PATH, POS

    jump = 30

    if POS + jump * dt <= len(PATH):
        POS += jump * dt
    else:
        POS = 0

    print(POS, time.time())



if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
