import pyglet
import random

from pyglet.gl import *

from utils.colors import random_color
from utils.shapes import circle
from utils.gl import enable_antialiasing


FPS = 60
WIDTH, HEIGHT = 800, 600
WALLCOLLISION = True


class Entity(object):

    def __init__(self, x, y, color, radius=10):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

        self.speed_x = (random.random() - 0.5) * 1000
        self.speed_y = (random.random() - 0.5) * 1000

    def update(self, dt):

        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        if WALLCOLLISION:
            if self.x - self.radius + 5 < 0 or self.x + self.radius + 5 > WIDTH:
                self.speed_x *= -1
            if self.y - self.radius + 5 < 0 or self.y + self.radius + 5 > HEIGHT:
                self.speed_y *= -1


    def draw(self):
        circle((self.x, self.y), radius=self.radius, color=self.color).draw(pyglet.gl.GL_LINE_LOOP)


class SandboxWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(caption='Pyglet Sandbox', width=WIDTH, height=HEIGHT)
        pyglet.clock.schedule_interval(self.update, 1.0 / FPS)

        pyglet.gl.glClearColor(0, 0, 0, 255)

        self.entities = []

        pyglet.app.run()

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)

    def on_draw(self):
        self.clear()

        enable_antialiasing()
        glLineWidth(5)

        for entity in self.entities:
            entity.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1:
            entity = Entity(x, y, random_color())
            self.entities.append(entity)


if __name__ == '__main__':
    SandboxWindow()
