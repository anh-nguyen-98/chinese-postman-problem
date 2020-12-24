"""
This module deals with retrieving the shortest distance/ path among nodes in graph.

author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""

from graph_shortest_path.dijkstra import Graph
import pandas as pd

"""
Param:  (str) filename csv file stores graph adjacency matrix
        (Nx Multigraph) G graph  

Returns distances the shortest distance between each source node to other nodes in graph.        
"""


def find_shortest_distance(filename, G):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    list_of_rows = [list(row)[1:] for row in data.values]
    g = Graph(len(G.nodes))
    g.graph = list_of_rows
    distances = g.length_from_source()
    return distances


"""
Param:  (str) filename csv file stores graph adjacency matrix
        (Nx Multigraph) G graph

Returns shortest paths (ordering of edges) each source node to other nodes in graph.
"""


def find_shortest_path(filename, G):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    list_of_rows = [list(row)[1:] for row in data.values]
    g = Graph(len(G.nodes))
    g.graph = list_of_rows
    path = g.path()
    return path


"""
"""

"""

Param:  G (Nx Multigraph) G graph,
        pairings (ls) list of all possible pairings (combinations) of odd-degree vertices , 
        distance (ls) the shortest distance between each source node to other nodes in graph, 
        filename (str) filename csv file stores graph adjacency matrix
Returns a detailed path connecting one subpair of nodes in graph  
"""


def previous_vertex(G, pairings, distance, filename):
    node_ids = find_node_ids(G)
    shortest_pairing = find_shortest_pairing(G, pairings, distance)
    path = find_shortest_path(filename, G)

    previous_vertices = []
    for sub_pair in pairings[shortest_pairing]:
        src = node_ids.get(sub_pair[0])
        des = node_ids.get(sub_pair[1])
        pair_path = path[src]

        src_to_des = []
        src_to_des.append(des)
        while src_to_des[0] != src:
            prev = pair_path[src_to_des[0]]
            src_to_des.insert(0, prev)

        previous_vertices.append(src_to_des)
    print(previous_vertices)

    for i in range(len(previous_vertices)):
        for j in range(len(previous_vertices[i])):
            for keys in node_ids:
                if node_ids[keys] == previous_vertices[i][j]:
                    previous_vertices[i][j] = keys
    print(previous_vertices)
    return previous_vertices


"""
Param:  (Nx Multigraph) G graph
Returns (dict) node_ids map str node with int node  
"""


def find_node_ids(G):
    node_ids = {}
    i = 0
    for node in G.nodes:
        node_ids[node] = i
        i += 1

    return node_ids


"""
Param:  pairing: (ls) list of subpair in one combination 
        node_ids: (dict) map between str node to int node
        distance: (ls) the shortest distance between each source node to other nodes in graph
        
Returns total path length connecting each subpair in (combination) of odd-deg vertex
"""


def len_path(pairing, node_ids, distance):
    len = 0
    for sub_pair in pairing:
        src = node_ids.get(sub_pair[0])
        des = node_ids.get(sub_pair[1])
        len += distance[src][des]

    return len


"""
Param:  G: graph
        pairings: list of all possible combinations of odd-deg vertices
        distance: (ls) the shortest distance between each source node to other nodes in graph
        
Returns (int) index of pairing with minimum shortest path connecting subpairs
"""


def find_shortest_pairing(G, pairings, distance):
    node_ids = find_node_ids(G)
    ret = 0
    min_len = len_path(pairings[0], node_ids, distance)
    for i in range(1, len(pairings)):
        if len_path(pairings[i], node_ids, distance) < min_len:
            ret = i

    return ret
