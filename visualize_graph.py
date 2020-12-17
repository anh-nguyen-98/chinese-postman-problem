"""
Visualize graph
"""

# visualize graph with turtle
import tkinter as tk
from io import BytesIO
from turtle import TurtleScreen, RawTurtle

import networkx as nx
from PIL import Image, ImageTk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# root = tk.Tk()
#
#
# x_coordinates = []
# y_coordinates = []
# for i in pos.keys():
#     x_coordinates += [pos[i][0]]
#     y_coordinates += [pos[i][1]]
#
# # Plot graph
# figure = Figure(figsize=(5, 5))
# subplot = figure.add_subplot(111)
# x = np.array(x_coordinates)
# y = np.array(y_coordinates)
# subplot.plot(x, y)
#
# # Make memory image of graph
# invisible_figure_canvas = FigureCanvasTkAgg(figure, root)
# buffer = BytesIO()
# figure.savefig(buffer, format="png")
# buffer.seek(0)
#
# # Open memory as tkinter image
# image = Image.open(buffer)
# photoImage = ImageTk.PhotoImage(image)
# buffer.close()
#
# # Now do our turtle drawing embedded in tkinter
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
#
# screen = TurtleScreen(canvas)
# screen._setbgpic(screen._bgpic, photoImage)  # bypass restrictions (protected access)
#
# turtle = RawTurtle(screen, shape='turtle')
# turtle.shapesize(4)
#
# def route (turtle, x_coordinates, y_coordinates):
#     for x, y in zip(x_coordinates, y_coordinates):
#         turtle.goto(x, y)
#
# route(turtle, x_coordinates, y_coordinates)
#
# screen.mainloop()


from graph_shortest_path.shortest_pairing import find_node_ids


def track_route(G):
    n = len(G.nodes)

    # construct incidence matrix (nxn): entry(i, j): occureences of edge (i, j)
    incidence_mx = np.zeros((n, n), dtype=int)
    node_ids = find_node_ids(G)
    for e in G.edges:
        u = node_ids.get(e[0])
        v = node_ids.get(e[1])
        incidence_mx[u][v] += 1
        incidence_mx[v][u] += 1

    #track route recursively
    route = track_route_helper([], incidence_mx, 0)

    #map int vertex back to str vertex
    int_to_str = list(G.nodes)
    for i in range(len(route)):
        route[i] = int_to_str[route[i]]

    return route



def track_route_helper(route, incidence_mx, v):
    nxt = find_nxt(v, incidence_mx)
    while nxt != -1:
        incidence_mx[v][nxt] -= 1
        incidence_mx[nxt][v] -= 1
        track_route_helper(route, incidence_mx, nxt)
        nxt = find_nxt(v, incidence_mx)

    route.insert(0, v)
    return route


def find_nxt(v, incidence_mx):
    for i in range(incidence_mx.shape[0]):
        if incidence_mx[v][i] > 0:
            return i

    return -1
