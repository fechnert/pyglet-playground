from math import *
from pyglet.gl import *


class Circle(object):
    points = 3


window = pyglet.window.Window()
circle = None


def makeCircle(numPoints):
    verts = []

    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = 100*cos(angle) + 100
        y = 100*sin(angle) + 100
        verts += [x,y]

    global circle
    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))


@window.event
def on_draw():
    glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,0)

    global circle
    circle.draw(GL_LINE_LOOP)


def update(gt):
    Circle.points += 1
    makeCircle(Circle.points)


if __name__ == '__main__':
    makeCircle(3)

    pyglet.clock.schedule_interval(update, 1/4.0)
    pyglet.app.run()
