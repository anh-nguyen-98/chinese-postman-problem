"""
turtle combine with graph
author: cdlane (stackover)
"""

import tkinter as tk
from io import BytesIO
from turtle import TurtleScreen, RawTurtle
from PIL import Image, ImageTk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

# Plot graph
figure = Figure(figsize=(5, 5))
subplot = figure.add_subplot(111)
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
subplot.plot(x, y)

# Make memory image of graph
invisible_figure_canvas = FigureCanvasTkAgg(figure, root)
buffer = BytesIO()
figure.savefig(buffer, format="png")
buffer.seek(0)

# Open memory as tkinter image
image = Image.open(buffer)
photoImage = ImageTk.PhotoImage(image)
buffer.close()

# Now do our turtle drawing embedded in tkinter
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

screen = TurtleScreen(canvas)
screen._setbgpic(screen._bgpic, photoImage)  # bypass restrictions (protected access)

turtle = RawTurtle(screen, shape='turtle')
turtle.shapesize(0.5)

def hilbertCurve(n, angle):
    if n <= 0:
        return

    turtle.left(angle)
    hilbertCurve(n - 1, -angle)
    turtle.forward(10)
    turtle.right(angle)
    hilbertCurve(n - 1, angle)
    turtle.forward(10)
    hilbertCurve(n - 1, angle)
    turtle.right(angle)
    turtle.forward(10)
    hilbertCurve(n - 1, -angle)
    turtle.left(angle)

hilbertCurve(4, 90)

screen.mainloop()