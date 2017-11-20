import pyglet
import random


window = pyglet.window.Window(
    width=800,
    height=600,
    caption='Python Paths',
)
window.clear()


P0 = [100, 100]
P1 = [100, 250]
P2 = [200, 250]
P3 = [200, 400]


def B(coordinate_array, i, j, t):
    if j == 0:
        return coordinate_array[i]
    return B(coordinate_array, i, j-1, t) * (1-t) + B(coordinate_array, i+1, j-1, t) * t


@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()

    batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (P0[0], P0[1], P1[0], P1[1])), ('c3B', (255, 0, 0, 255, 0, 0)))
    batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (P2[0], P2[1], P3[0], P3[1])), ('c3B', (255, 0, 0, 255, 0, 0)))

    coordinate_array_x = [P0[0], P1[0], P2[0], P3[0]]
    coordinate_array_y = [P0[1], P1[1], P2[1], P3[1]]

    steps = 1000
    for k in range(steps):
        t = float(k) / (steps - 1)
        x = int(B(coordinate_array_x, 0, 4-1, t))
        y = int(B(coordinate_array_y, 0, 4-1, t))

        batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', (x, y)), ('c3B', (0, 255, 0)))

    batch.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    P0[0] = x
    P0[1] = y
    P1 = (x, y + 150)


def update(dt):
    pass


if __name__ == '__main__':
    pyglet.app.run()
