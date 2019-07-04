import numpy as np
import cairo

points = [np.array([1,1]), np.array([1,0]), np.array([0,0]), np.array([0,1])]

dt = 0.1

print(points)

def copy_points(points):
    res = []
    for p in points:
        res.append(np.copy(p))
    return res

def bezier(p, t):
    points = copy_points(p)
    i = len(points) - 1
    for x in range(i):
        for y in range(i - x):
            a = points[y] * (1 - t)
            b = points[y + 1] * t
            points[y] = a + b
    return points[0]



WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.move_to(points[0][0], points[0][1])

for i in np.arange(0, 1, dt):
    p = bezier(points, i)
    print(i)
    print("points: " + str(points))
    print("p: " + str(p))
    ctx.move_to(p[0], p[1])

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
