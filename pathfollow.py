import pyglet
import random

from utils import get_line_path, get_bezier_path


window = pyglet.window.Window(
    width=800,
    height=600,
    caption='Python Paths',
)
window.clear()

PATH = []

@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()

    path = get_bezier_path([(100, 100), (200, 300), (300, 100)])

    for point in path:
        batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', point), ('c3B', (0, 255, 0)))

    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
