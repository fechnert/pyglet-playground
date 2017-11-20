def get_line_path(start, end):
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


def get_bezier_path(points):
    path = []

    def B(coordinate_array, i, j, t):
        if j == 0:
            return coordinate_array[i]
        return B(coordinate_array, i, j-1, t) * (1-t) + B(coordinate_array, i+1, j-1, t) * t

    coordinate_array_x = []
    coordinate_array_y = []

    for point in points:
        print(point)
        coordinate_array_x.append(point[0])
        coordinate_array_y.append(point[1])

    steps = 1000
    for k in range(steps):
        t = float(k) / (steps - 1)
        x = int(B(coordinate_array_x, 0, len(points)-1, t))
        y = int(B(coordinate_array_y, 0, len(points)-1, t))
        path.append((x, y))

    return path
