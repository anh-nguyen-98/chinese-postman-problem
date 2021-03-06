"""
The module visualizes the shortest route through all edges in graph using Python turtle.

author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import turtle
import networkx as nx
import numpy as np
from shortest_pairing import find_node_ids

"""

Param: G(Nx Multigraph) graph (edges already modified for non-eulerian)
Returns a visualization of the shortest route through all edges in graph using Python turtle.
"""


def visualize_route(G):
    pos = nx.spring_layout(G)
    visited = []
    coordinates = []
    route = track_route(G)
    for nodes in route:
        coordinates += [list(pos[nodes])]
        turtle.shape('turtle')
        turtle.penup()
        turtle.goto(coordinates[0][0] * 300, coordinates[0][1] * 300)
    for i in range(len(coordinates)):
        turtle.pendown()
        turtle.color('black')
        turtle.stamp()
        turtle.goto(coordinates[i][0] * 300, coordinates[i][1] * 300)

    for i in range(1, len(coordinates)):
        edge = list(zip(route[i], route[i - 1]))
        if edge[0] in visited or edge[0][::-1] in visited:
            turtle.pendown()
            turtle.color('red')
            turtle.speed('slowest')
            turtle.stamp()
            turtle.pensize(3)
            turtle.goto(coordinates[i][0] * 300, coordinates[i][1] * 300)
        else:
            turtle.pendown()
            turtle.color('blue')
            turtle.speed('slowest')
            turtle.stamp()
            turtle.pensize(3)
            turtle.goto(coordinates[i][0] * 300, coordinates[i][1] * 300)
            visited += edge

    turtle.Screen().exitonclick()

"""
Param: G (Nx Multigraph) graph (edges already modified for non-eulerian)
Returns the (ls) ordering of vertices & edges for turtle to visit
"""


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

    # track route recursively
    route = track_route_helper([], incidence_mx, 0)

    # map int vertex back to str vertex
    int_to_str = list(G.nodes)
    for i in range(len(route)):
        route[i] = int_to_str[route[i]]

    return route

"""
Helper method for track_route 

@:parameter route: returned route
            incidenece_mx: matrix keeing the number of unvisited edge 
            v: vertex
"""
def track_route_helper(route, incidence_mx, v):
    nxt = find_nxt(v, incidence_mx)
    while nxt != -1:
        incidence_mx[v][nxt] -= 1
        incidence_mx[nxt][v] -= 1
        track_route_helper(route, incidence_mx, nxt)
        nxt = find_nxt(v, incidence_mx)

    route.insert(0, v)
    return route


"""
Helper method for track_route_helper

@:parameter: v: vertex 
             incidence_mx: matrix keeing the number of unvisited edge 
Returns the next unvisited edge from a vertex v 
"""
def find_nxt(v, incidence_mx):
    for i in range(incidence_mx.shape[0]):
        if incidence_mx[v][i] > 0:
            return i

    return -1
