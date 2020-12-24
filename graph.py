"""
The module constructs a Multigraph object (Networkx) from
adjacency matrix (csv).

author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import networkx as nx
import pandas as pd
import turtle
import matplotlib.pyplot as plt
from visualize_graph import track_route

"""
Param:  (str) csv file path storing graph adjacency matrix. 
        Entry (i, j) in matrix stores weight of edge {i, j}. 

Returns a Multigraph object (Networkx) with data 
for nodes, weighted edges
"""


def retrieve_graph(filename):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    G = nx.MultiGraph()
    G.add_nodes_from(data.columns[1:])

    for row in data.index.array:
        for col in data.columns[row + 1:]:
            # data = data.fillna(0)
            if data.iloc[row][col] != 0:
                G.add_edge(data.iloc[row][0], col, weight=data.iloc[row][col])
    return G

