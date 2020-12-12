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

def get_coordinates(G):
    edges = []
    for e in G.edges():
        s = set()
        for v in e:
            s.add(v)
        edges.append(s)
    print (edges)
    # pos = nx.spring_layout(G)

    # xy_pos = []
    #
    # e1 = edges.pop(0)
    # xy_pos.append(pos[e1[0]])
    # xy_pos.append(pos[e1[1]])
    #
    # while edges:
    #     for i in edges:
    #         if e1[1] in i:
    #             v = e1[1]
    #             e1 = edges.remove(i)
    #             for vertex in e1:
    #                 if vertex != v:
    #                     xy_pos.append(pos[vertex])
    #
    #
    #
    # print(xy_pos)

    ordered_vertices = []
    # edges = set(G.edges())
    #edges: list of set
    e1 = edges.pop(0)

    for v in e1:
        ordered_vertices.append(v)

    last_visited = ordered_vertices[-1]
    while edges != []:
        e1_id = find_edge_containing_vertex(last_visited, edges)
        e1 = edges[e1_id]
        print(e1)

        e1.remove(last_visited)
        last_visited = e1.pop()
        ordered_vertices.append(last_visited)
        edges.pop(e1_id)
        print(edges)
        print()

    return ordered_vertices





def find_edge_containing_vertex (vertex, edges):
    for i in range(len(edges)):
        if vertex in edges[i]:
            return i










