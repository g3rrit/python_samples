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

for p in paths:
    for x in np.arange(0, 1, 0.01):
        print(type(p.point(x)))
        print(p.point(x).real)
        print(p.point(x).imag)
        ctx.arc(p.point(x).real, p.point(x).imag, 0.01, 2 * math.pi)
        ctx.fill()


surface.write_to_png("example.png")  # Output to PNG
