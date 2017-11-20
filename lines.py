import pyglet
import random


window = pyglet.window.Window(
    width=640,
    height=480,
    caption='Python Paths',
)
window.clear()


START = (100, 100)
END = (150, 50)


@window.event
def on_draw():
    window.clear()

    batch = pyglet.graphics.Batch()

    batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', START), ('c3B', (0, 255, 0)))
    batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', END), ('c3B', (255, 0, 0)))

    points = get_line(START, END)
    for point in points:
        batch.add(1, pyglet.gl.GL_POINTS, None, ('v2f', point))

    batch.add(2, pyglet.gl.GL_LINES, None,
        ('v2f', (START[0] + 10, START[1], END[0] + 10, END[1])),
        ('c3B', (255, 0, 0, 255, 0, 0)),
    )

    batch.draw()


def get_line(start, end):
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


def update(dt):
    pass


if __name__ == '__main__':
    pyglet.app.run()
