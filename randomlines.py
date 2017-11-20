import pyglet
import random


window = pyglet.window.Window(
    width=640,
    height=480,
    caption='Python Paths',
)
window.clear()


@window.event
def on_draw():
    window.clear()

    batch = pyglet.graphics.Batch()

    for i in range(10):
        src_x = random.randint(0, window.width)
        src_y = random.randint(0, window.height)
        dst_x = random.randint(0, window.width)
        dst_y = random.randint(0, window.height)

        batch.add(
            2,
            pyglet.gl.GL_LINES,
            None,
            ('v2f', (src_x, src_y, dst_x, dst_y)),
            ('c3B', (255, 0, 0, 0, 255, 0)),
        )

    batch.draw()


def update(dt):
    pass


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/16.0)
    pyglet.app.run()
