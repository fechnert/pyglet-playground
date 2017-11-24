import pyglet
import random

from pyglet.gl import *

from utils.colors import Nice16, random_color
from utils.shapes import circle
from utils.gl import enable_antialiasing


FPS = 60
WIDTH, HEIGHT = 800, 600


class Entity(object):

    def __init__(self, position=(WIDTH//2, HEIGHT//2), color=(255, 255, 255), speed=2, radius=10, filled=False):
        self.position = position
        self.color = color
        self.speed = speed
        self.radius = radius
        self.filled = filled

        self.target = (None, None)
        self.delta = (None, None)

    def update(self, dt, target):

        if target == (None, None):
            return

        delta = (
            target[0] - self.position[0],
            target[1] - self.position[1]
        )

        self.position = (
            self.position[0] + (delta[0] * self.speed * dt),
            self.position[1] + (delta[1] * self.speed * dt)
        )

    def draw(self):
        circle(self.position, radius=self.radius, color=self.color).draw(GL_POLYGON if self.filled else GL_LINE_LOOP)


class SandboxWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(caption='Pyglet Sandbox', width=WIDTH, height=HEIGHT)
        pyglet.clock.schedule_interval(self.update, 1.0 / FPS)

        pyglet.gl.glClearColor(0, 0, 0, 255)

        self.entities = [
            Entity((WIDTH//2-100, HEIGHT//2+100), speed=2, color=Nice16.blue),
            Entity((WIDTH//2+100, HEIGHT//2+100), speed=3, color=Nice16.red),
            Entity((WIDTH//2-100, HEIGHT//2-100), speed=4, color=Nice16.lime),
            Entity((WIDTH//2+100, HEIGHT//2-100), speed=5, color=Nice16.fuchsia),
        ]

        self.cursor_pos = (None, None)
        self.pause = False

        pyglet.app.run()

    def update(self, dt):
        if self.pause:
            return

        for entity in self.entities:
            entity.update(dt, self.cursor_pos)

    def on_draw(self):
        self.clear()

        enable_antialiasing()
        glLineWidth(3)

        for entity in self.entities:
            entity.draw()

        if self.pause:
            pyglet.text.Label('PAUSED', font_size=15, x=WIDTH//2, y=HEIGHT//2, anchor_x='center', anchor_y='center').draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_pos = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1:
            entity = Entity((x, y), speed=random.random()*10, color=random_color())
            self.entities.append(entity)

    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol == pyglet.window.key.SPACE:
            self.pause = not self.pause


if __name__ == '__main__':
    SandboxWindow()
