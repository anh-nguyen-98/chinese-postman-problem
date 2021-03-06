"""
Discrete math final project
The program finds the shortest walk to visit all edges of a graph
and uses Python turtle to visualize.
(Solution to Chinese Postman Problem)

author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import networkx as nx
import matplotlib.pyplot as plt
from pandas.core.indexes import multi
from networkx.drawing.nx_agraph import write_dot

from check_eulerian import is_eulerian
import turtle
import graph
import graphviz
import pydot
from networkx.drawing.nx_pydot import write_dot

from graph_shortest_path.shortest_pairing import find_shortest_path
from graph_shortest_path.shortest_pairing import find_shortest_distance
from graph_shortest_path.shortest_pairing import previous_vertex
from graph_shortest_path.odd_degree_pairing import get_odd_degree_list, pairing_vertex
from graph_shortest_path.shortest_pairing import find_shortest_pairing
# from visualize_graph import get_coordinates
from visualize_graph import track_route, visualize_route

"""
Returns the shortest walk on the graph. 

:param: (str) name of the excel file that stores a graph. 
   
"""


def get_shortest_walk (filename):
    # retrieves graph from csv
    # filename = "graph 1.csv"
    G = graph.retrieve_graph(filename)

    # deals with non-eulerian graph:
    if not is_eulerian(G):
        # gets list of odd-degree vertices
        odd_degree_list = get_odd_degree_list(G)

        # gets combinations (pairings) of odd-degree vertices
        pairings = pairing_vertex(odd_degree_list, [], [], len(odd_degree_list))

        # implements Dijkstra algorithm to find shortest distance from each source node
        # to other nodes in graph
        distances = find_shortest_distance(filename, G)

        # return id of pairing with minimum shortest path connecting subpairs
        shortest_pairing = find_shortest_pairing(G, pairings, distances)

        # returns shortest paths (ordering of edges) connecting each subpair
        #  in shortest pairing
        path = find_shortest_path(filename, G)

        # adds the found edges to graph
        previous_vertices = previous_vertex(G, pairings, distances, filename)
        new_edges = []
        for i in range(len(previous_vertices)):
            new_edges = list(zip(previous_vertices[i], previous_vertices[i][1:]))
        for edge in new_edges:
            if edge in G.edges:
                G.add_edge(edge[0], edge[1])
                G[edge[0]][edge[1]][1]['weight'] = G[edge[0]][edge[1]][0]['weight']

    # visualize shortest route with turtle
    visualize_route(G)

