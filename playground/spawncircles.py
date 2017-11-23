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

    def __init__(self, x, y, color=(255, 255, 255), speed_x=0.25, speed_y=0.25, radius=10, filled=False):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.filled = filled

    def update(self, dt):

        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        if WALLCOLLISION:

            if self.x - self.radius <= 0:
                self.speed_x = abs(self.speed_x)
            if self.x + self.radius >= WIDTH:
                self.speed_x = -self.speed_x

            if self.y - self.radius <= 0:
                self.speed_y = abs(self.speed_y)
            if self.y + self.radius >= HEIGHT:
                self.speed_y = -self.speed_y


    def draw(self):
        circle((self.x, self.y), radius=self.radius, color=self.color).draw(GL_POLYGON if self.filled else GL_LINE_LOOP)


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
            entity = Entity(
                x, y, random_color(),
                speed_x=(random.random() - 0.5) * 1000,
                speed_y=(random.random() - 0.5) * 1000,
                radius=random.randint(10, 15),
                filled=random.choice([True, False])
            )
            self.entities.append(entity)


if __name__ == '__main__':
    SandboxWindow()
