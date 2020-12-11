"""
Visualize graph
"""

#visualize graph with turtle 
import tkinter as tk
from io import BytesIO
from turtle import TurtleScreen, RawTurtle
from PIL import Image, ImageTk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
root = tk.Tk()


x_coordinates = []
y_coordinates = []
for i in pos.keys():
    x_coordinates += [pos[i][0]]
    y_coordinates += [pos[i][1]]

# Plot graph
figure = Figure(figsize=(5, 5))
subplot = figure.add_subplot(111)
x = np.array(x_coordinates)
y = np.array(y_coordinates)
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
turtle.shapesize(4)

def route (turtle, x_coordinates, y_coordinates):
    for x, y in zip(x_coordinates, y_coordinates):
        turtle.goto(x, y)
        
route(turtle, x_coordinates, y_coordinates)

screen.mainloop()