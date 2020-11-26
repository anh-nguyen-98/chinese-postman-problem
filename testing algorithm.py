
"""
Discrete math final project
author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""


"""
    Accomplishments so far:
        read csv file for graph data
        check if eulerian
        draw graph on networkx
        length path
        odd degree list
        possible pairing between odd degree vertices
"""
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

filename = "graph 1.csv"
with open(filename, 'r') as in_file:
    data = pd.read_csv(filename)
    
G = nx.Graph()
G.add_nodes_from(data.columns[1:])

for row in data.index.array:
    for col in data.columns[1:]:
        data = data.fillna(0)
        if data.iloc[row][col] != 0:
            G.add_edge(data.iloc[row][0], col, weight = data.iloc[row][col])
   
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
plt.axis("off")

def is_eulerian (G):
    degree_list = [val for (node, val) in G.degree()]
    for i in degree_list:
        if i %2 == 1:
            return False
    return True
        
#Get length path: 
def get_length_path (G): 
    total_weight = 0
    for edge in G.edges:
        total_weight += G.get_edge_data(edge[0], edge[1])["weight"]
    return total_weight

#step 2: list of odd-deree vertices:
def get_odd_degree_list(G): 
    odd_degree_list = []
    #degree_list = [val for (node, val) in G.degree()]
    for i in G.degree():
        if i[1] % 2 == 1:
            odd_degree_list.append(i[0])
    return odd_degree_list

#step 3:

#odd_degree_list = (A, B, C, D)
#=> 3 ways to pair
#1: A-B, C-D

#2: A-C, B-D

#3: A-D, B-C
pairings = []
odd_degree_list = get_odd_degree_list(G)
current_pairing = []
def pairing_vertex(pairings, odd_degree_list, current_pairing):
    if odd_degree_list == []:
        odd_degree_list.append(current_pairing)
        return odd_degree_list
    first = odd_degree_list[0]
    rest= odd_degree_list[1:]
    for i in range(len(rest)):
        pair_1 = tuple(zip(first, rest[i]))
        current_pairing += [pair_1]
        pairing_vertex(pairings, rest[1], current_pairing)
        
    return pairings or pairing_vertex(rest)



