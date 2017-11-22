import pyglet
import random

from utils.colors import random_color
from utils.shapes import circle


FPS = 60
#WALLCOLLISION = False


class Entity(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

        self.speed_x = (random.random() - 0.5) * 1000
        self.speed_y = (random.random() - 0.5) * 1000

    def update(self, dt):
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

    def draw(self):
        circle((self.x, self.y)).draw(pyglet.gl.GL_LINE_LOOP)


class SandboxWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(caption='Pyglet Sandbox', width=800, height=600)
        pyglet.clock.schedule_interval(self.update, 1.0 / FPS)

        pyglet.gl.glClearColor(0, 0, 0, 255)

        self.entities = []

        pyglet.app.run()

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)

    def on_draw(self):
        self.clear()

        for entity in self.entities:
            entity.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1:
            entity = Entity(x, y, random_color())
            self.entities.append(entity)


if __name__ == '__main__':
    SandboxWindow()
