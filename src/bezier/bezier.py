import numpy as np
import cairo

points = [np.array([1,1]), np.array([1,0]), np.array([0,0]), np.array([0,1])]

dt = 0.01

print(points)

def copy_points(dst, src):
    print("dl: " + str(len(dst)) + " sl: " + str(len(src)))
    if(len(dst) != len(src)):
        raise Exception("trying to copy arrays of different length")
    for i in range(len(src)):
        dst[i] = np.copy(src[i])

def bezier_point(p, t, buf):
    copy_points(buf, p)
    i = len(points) - 1
    for x in range(i):
        for y in range(i - x):
            a = buf[y] * (1 - t)
            b = buf[y + 1] * t
            buf[y] = a + b
    return buf[0]

def bezier(p, dt):
    buf = [None] * len(p)
    print("here")
    for i in np.arange(dt, 1 + dt, dt):
        p = bezier_point(p, i, buf)
        yield p

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.move_to(points[0][0], points[0][1])

for p in bezier(points, dt):
    print("points: " + str(points))
    print("p: " + str(p[0]) + " " + str(p[1]))
    ctx.line_to(p[0], p[1])


ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
