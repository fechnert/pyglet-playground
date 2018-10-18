"""
First attempt to draw and rotate custom shapes.

TODO: improve debug output
TODO: use batches to optimize drawing of similar shapes
TODO: make the spaceship accelerate and breake
TODO: respect spaceship angle while moving
TODO: add different entities like asteroids
TODO: make the spaceship shoot lasers
TODO: let the lasers collide with asteorids
TODO: react on the collision of entities or lasers
TODO: differentiate between the coordinate grid and the visible section of the window
TODO: add scaling of visible section to allow zooming

2D collision detection:
  - https://developer.mozilla.org/kab/docs/Games/Techniques/2D_collision_detection
  - https://www.robloxdev.com/articles/2D-Collision-Detection
  - https://www.sevenson.com.au/actionscript/sat/

"""

import pyglet

from math import sin, cos, radians

from utils.gl import enable_antialiasing


FPS = 30
WIDTH, HEIGHT = 800, 600


def debug(x, y, text, color=(255, 255, 255, 255), size=8):
    pyglet.text.Label(text, font_size=size, x=x, y=y, font_name='Courier', color=color).draw()


class Entity(object):

    def __init__(self, x, y, angle=0, color=(255, 255, 255)):
        self.center = (x, y)
        self.angle = angle
        self.color = color

    shape = [
        (0, -200), (100, 100), (0, 50), (-100, 100)
        #(100, -100), (100, 100), (-100, 100), (-100, -100)
    ]

    def update(self, dt):
        if self.angle < 360:
            self.angle += 1
        else:
            self.angle = 0

    def draw(self):

        debug(10, 10, 'Angle: {}'.format(self.angle))

        vertex = []
        for i, coords in enumerate(self.shape):
            _x = coords[0]
            _y = coords[1]

            angle = radians(self.angle)

            x = _x * cos(angle) - _y * sin(angle)
            y = _x * sin(angle) + _y * cos(angle)

            x = self.center[0] + x
            y = self.center[1] + y

            vertex += [x, y]
            debug(x, y, str(i), size=15, color=(255,0,0,128))

        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2f', (self.center)), ('c4B', (0,255,0,128)))
        pyglet.graphics.vertex_list(len(vertex) // 2, ('v2f', vertex)).draw(pyglet.gl.GL_LINE_LOOP)


class SimulationWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(caption='Spaceship simulation', width=WIDTH, height=HEIGHT)
        pyglet.clock.schedule_interval(self.update, 1.0 / FPS)

        pyglet.gl.glClearColor(0, 0, 0, 255)

        self.entities = []
        self.pause = False

    def run(self):
        pyglet.app.run()

    def update(self, dt):
        if self.pause:
            return

        for entity in self.entities:
            entity.update(dt)

    def on_draw(self):
        self.clear()
        enable_antialiasing()

        for entity in self.entities:
            entity.draw()

        if self.pause:
            pyglet.text.Label('PAUSED', font_size=15, x=WIDTH//2, y=HEIGHT//2, anchor_x='center', anchor_y='center').draw()

    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)

        if symbol == pyglet.window.key.SPACE:
            self.pause = not self.pause


if __name__ == '__main__':
    window = SimulationWindow()
    window.entities = [
        Entity(300, 300)
    ]

    window.run()
