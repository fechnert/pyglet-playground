import pyglet
import random
from math import cos, sin, radians


window = pyglet.window.Window(
    width=800,
    height=600,
    caption='Python Paths',
    #fullscreen=True
)
window.set_mouse_visible(False)
window.clear()

POINTER = [100, 100]
MARKS = []


def get_circle_vertex(points, batch):
    verts = []

    for i in range(points):
        angle = radians(float(i) / points * 360.0)
        x = 10 * cos(angle) + POINTER[0]
        y = 10 * sin(angle) + POINTER[1]
        verts += [x, y]

    #return pyglet.graphics.vertex_list(points, ('v2f', verts))
    batch.add(points, pyglet.gl.GL_LINE_LOOP, None, ('v2f', verts))


@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()

    get_circle_vertex(36, batch)

    lx, ly = None, None
    for mark in MARKS:
        if lx and ly:
            batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', [lx, ly] + mark))
        lx, ly = mark

    if lx and ly:
        batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', [lx, ly] + POINTER))

    batch.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    POINTER[0] = x
    POINTER[1] = y


@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    POINTER[0] = x
    POINTER[1] = y


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == 1:
        MARKS.append([x, y])


if __name__ == '__main__':
    pyglet.app.run()
