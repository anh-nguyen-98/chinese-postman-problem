"""

"""

from graph_shortest_path.dijkstra import Graph
import pandas as pd


def find_shortest_distance(filename, G):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    list_of_rows = [list(row)[1:] for row in data.values]
    g = Graph(len(G.nodes))
    g.graph = list_of_rows
    distances = g.length_from_source()
    return distances


def find_shortest_path(filename, G):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    list_of_rows = [list(row)[1:] for row in data.values]
    g = Graph(len(G.nodes))
    g.graph = list_of_rows
    path = g.path()
    return path

def find_node_ids(G):
    node_ids = {}
    i = 0
    for node in G.nodes:
        node_ids[node] = i
        i += 1

    return node_ids

def len_path (pairing, node_ids, distance):
    len = 0
    for sub_pair in pairing:
        src = node_ids.get(sub_pair[0])
        des = node_ids.get(sub_pair[1])
        len += distance[src][des]

    return len


def find_shortest_pairing (G, pairings, distance):
    node_ids = find_node_ids(G)
    ret = 0
    min_len = len_path(pairings[0], node_ids, distance)
    for i in range(1, len(pairings)):
        if len_path(pairings[i], node_ids, distance) < min_len:
            ret = i

    return ret
    
def previous_vertex(G, pairings, distance, filename):
    node_ids = find_node_ids(G)
    shortest_pairing = find_shortest_pairing(G, pairings, distance)
    path  = find_shortest_path(filename, G)
    
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
    
    
    
    