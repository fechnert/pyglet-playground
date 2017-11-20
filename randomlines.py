import pyglet
import random

from pyglet.gl import *


def random_rgb():
    r255 = lambda: random.randint(0, 255)
    return (r255(), r255(), r255())

window = pyglet.window.Window(
    width=640,
    height=480,
    caption='Python Paths',
)
window.clear()

glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
glLineWidth(8)

@window.event
def on_draw():
    window.clear()

    batch = pyglet.graphics.Batch()

    for i in range(10):
        src_x = random.randint(0, window.width)
        src_y = random.randint(0, window.height)
        dst_x = random.randint(0, window.width)
        dst_y = random.randint(0, window.height)

        rgb1 = ()


        batch.add(
            2,
            GL_LINES,
            None,
            ('v2f', (src_x, src_y, dst_x, dst_y)),
            ('c3B', random_rgb() + random_rgb()),
        )

    batch.draw()

if __name__ == '__main__':
    pyglet.app.run()
