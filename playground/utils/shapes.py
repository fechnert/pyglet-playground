"""
Primitive shapes
"""

import pyglet

from math import radians, sin, cos


def circle(center_coord, radius=10, color=(255, 255, 255)):
    vert = []

    # should be okay i guess
    points = radius * 2

    for i in range(points):
        angle = radians(float(i) / points * 360.0)
        x = radius * cos(angle) + center_coord[0]
        y = radius * sin(angle) + center_coord[1]
        vert += [x, y]

    return pyglet.graphics.vertex_list(points, ('v2f', vert), ('c3B', color * points))


def line(start, end):
    """Draw lines with the Bresenham algorithm"""

    # Setup initial conditions
    src_x, src_y = start
    dst_x, dst_y = end
    delta_x = dst_x - src_x
    delta_y = dst_y - src_y

    # check if line is too steep
    is_steep = abs(delta_y) > abs(delta_x)

    # rotate line
    if is_steep:
        src_x, src_y = src_y, src_x
        dst_x, dst_y = dst_y, dst_x

    # Swap start and end points if necessary and store swap state
    swapped = False
    if src_x > dst_x:
        src_x, dst_x = dst_x, src_x
        src_y, dst_y = dst_y, src_y
        swapped = True

    # Recalculate differentials
    delta_x = dst_x - src_x
    delta_y = dst_y - src_y

    # Calculate error
    error = int(delta_x / 2.0)
    ystep = 1 if src_y < dst_y else -1

    # Iterate over bounding box generating points between start and end
    y = src_y
    points = []
    for x in range(src_x, dst_x + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(delta_y)
        if error < 0:
            y += ystep
            error += delta_x

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()

    return points


def bezier(points):
    """Draw an bézier curve"""

    path = []

    def B(coordinate_array, i, j, t):
        if j == 0:
            return coordinate_array[i]
        return B(coordinate_array, i, j-1, t) * (1-t) + B(coordinate_array, i+1, j-1, t) * t

    coordinate_array_x = []
    coordinate_array_y = []

    for point in points:
        coordinate_array_x.append(point[0])
        coordinate_array_y.append(point[1])

    steps = 250
    for k in range(steps):
        t = float(k) / (steps - 1)
        x = int(B(coordinate_array_x, 0, len(points)-1, t))
        y = int(B(coordinate_array_y, 0, len(points)-1, t))
        path.append((x, y))

    return path
