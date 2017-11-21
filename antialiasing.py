import pyglet
import random

from pyglet.gl import *

config = pyglet.gl.Config(sample_buffers=1, samples=8)
window = pyglet.window.Window(
    width=640,
    height=480,
    caption='Python Paths',
    config=config
)
window.clear()


@window.event
def on_draw():
    window.clear()

    glLineWidth(5)

    pyglet.graphics.draw(2, GL_LINES, ('v2f', (100, 120, 500, 170)))

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

    pyglet.graphics.draw(2, GL_LINES, ('v2f', (100, 100, 500, 150)))


if __name__ == '__main__':
    pyglet.app.run()
