from svgpathtools import svg2paths
import numpy as np
import math
import cairo

paths, attributes = svg2paths("example/note.svg")

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color

points = []
for p in paths:
    for x in np.arange(0, 1, 0.001):
        points.append(np.array([p.point(x).real, p.point(x).imag]))

def normalize(pa):
    xmax = 0
    ymax = 0
    for p in pa:
        if p[0] > xmax:
            xmax = p[0]
        if p[1] > ymax:
            ymax = p[1]

    for p in pa:
        p[0] = p[0] / xmax
        p[1] = p[1] / ymax


normalize(points)

for p in points:
    ctx.arc(p[0], p[1], 0.003, 0, 2 * math.pi)
    ctx.fill()


surface.write_to_png("example.png")  # Output to PNG
