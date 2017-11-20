import pyglet
import random


window = pyglet.window.Window(
    width=800,
    height=600,
    caption='Python Paths',
)
window.clear()


P0 = [100, 100]
P1 = [200, 300]
P2 = [300, 100]


def B(coordinate_array, i, j, t):
    if j == 0:
        return coordinate_array[i]
    return B(coordinate_array, i, j-1, t) * (1-t) + B(coordinate_array, i+1, j-1, t) * t


@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()

    coordinate_array_x = [P0[0], P1[0], P2[0]]
    coordinate_array_y = [P0[1], P1[1], P2[1]]

    steps = 1000
    for k in range(steps):
        t = float(k) / (steps - 1)
        x = int(B(coordinate_array_x, 0, 3-1, t))
        y = int(B(coordinate_array_y, 0, 3-1, t))

        batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', (x, y)), ('c3B', (0, 255, 0)))

    batch.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    P1[0] = x
    P1[1] = y


def update(dt):
    pass


if __name__ == '__main__':
    pyglet.app.run()
