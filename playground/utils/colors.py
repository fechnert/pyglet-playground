"""
Some color definitions
"""

import random


__all__ = ['random_color', 'Base16', 'Nice16']


def random_baseobject_color(baseobject):
    colors = [v for n, v in baseobject.__dict__.items() if not n.startswith('_')]
    i = random.randint(0, len(colors) - 1)
    return colors[i]


def random_color():
    r255 = lambda: random.randint(0, 255)
    return (r255(), r255(), r255())


class ColorSet(object):
    """Inherit from me if you specify an own color set"""

    @classmethod
    def random(self):
        return random_baseobject_color(self)


class Base16(ColorSet):
    """The basic 16 colors"""

    black   = (0,   0,   0)
    grey    = (128, 128, 128)
    silver  = (192, 192, 192)
    white   = (255, 255, 255)
    maroon  = (128, 0,   0)
    red     = (255, 0,   0)
    olive   = (128, 128, 0)
    yellow  = (255, 255, 0)
    green   = (0,   128, 0)
    lime    = (0,   255, 0)
    teal    = (0,   128, 128)
    aqua    = (0,   255, 255)
    navy    = (0,   0,   128)
    blue    = (0,   0,   255)
    purple  = (128, 0,   128)
    fuchsia = (255, 0,   255)


class Nice16(ColorSet):
    """Basic 16 colors, nicer (http://clrs.cc/)"""

    black   = (17,  17,  17)
    grey    = (170, 170, 170)
    silver  = (221, 221, 221)
    white   = (255, 255, 255)
    maroon  = (133, 20,  75)
    red     = (255, 65,  54)
    olive   = (61 , 153, 112)
    yellow  = (255, 220, 0)
    green   = (64,  204, 64)
    lime    = (1,   255, 112)
    teal    = (57,  204, 204)
    aqua    = (127, 219, 255)
    navy    = (0,   31,  63)
    blue    = (0,   116, 217)
    purple  = (117, 13,  201)
    fuchsia = (240, 18,  190)
