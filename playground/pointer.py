import pyglet
import random
from math import cos, sin, radians


window = pyglet.window.Window(
    width=800,
    height=600,
    caption='Python Paths',
    #fullscreen=True
)
#window.set_exclusive_mouse()  # WOW
window.set_mouse_visible(False)
window.clear()

COORD = [100, 100]

def get_circle_vertex(points):
    verts = []

    for i in range(points):
        angle = radians(float(i) / points * 360.0)
        x = 10 * cos(angle) + COORD[0]
        y = 10 * sin(angle) + COORD[1]
        verts += [x, y]

    return pyglet.graphics.vertex_list(points, ('v2f', verts))


@window.event
def on_draw():
    window.clear()
    get_circle_vertex(36).draw(pyglet.gl.GL_LINE_LOOP)


@window.event
def on_mouse_motion(x, y, dx, dy):
    COORD[0] = x
    COORD[1] = y

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    COORD[0] = x
    COORD[1] = y


if __name__ == '__main__':
    pyglet.app.run()
