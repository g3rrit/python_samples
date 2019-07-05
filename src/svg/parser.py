from svgpathtools import svg2paths
import numpy as np
import cairo

paths, attributes = svg2paths("example/note.svg")

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.move_to(points[0][0], points[0][1])

for p in paths:
    for x in np.arange(0, 1, 0.01):
        print(type(p.point(x)))
        print(p.point(x).real)
        print(p.point(x).imag)



ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
