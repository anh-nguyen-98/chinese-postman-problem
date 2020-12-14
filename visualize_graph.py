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


def track_route (G):
    #input: edges
    #degree list ()
    #visited edges
    #output: order of vertices visited

    #algorithm: DFS. once vertex has no outgoing edge, put to front of route > backtrack
    n = len(G.nodes)
    incidence_mx = np.zeros((n, n), dtype=int)

    node_ids = find_node_ids(G)
    for e in G.edges:
        u = node_ids.get(e[0])
        v = node_ids.get(e[1])
        incidence_mx[u][v] += 1
        incidence_mx[v][u] += 1

    m = len(G.edges)
    degree_arr = [node[1] for node in G.degree]
    route = []
    track_route_helper(route, incidence_mx, degree_arr, m, 0)
    print ('result: ')
    ids = "ABCDEFGH"
    ret = ''
    for i in route:
        ret += ids[i]
    print (ret)



def track_route_helper(route, incidence_mx, degree_arr, m, v):
    #base case:
    if m == 0:
        return

    # recursive
    print ('v: ' + str(v))
    print('degree[v]: ' + str(degree_arr[v]))
    while degree_arr[v] > 0:
        nxt = find_nxt(v, incidence_mx)
        print ('next'+ str(nxt))
        incidence_mx[v][nxt] -= 1
        incidence_mx[nxt][v] -= 1
        degree_arr[v] -= 1
        degree_arr[nxt] -= 1
        track_route_helper(route, incidence_mx, degree_arr, m-1, nxt)

    route.insert(0, v)
    print ('route' )
    print(route)
    return





def find_nxt (v, incidence_mx):
    print(incidence_mx.shape[0])
    for i in range(incidence_mx.shape[0]):
        if incidence_mx[v][i] > 0:
            return i

    return -1









