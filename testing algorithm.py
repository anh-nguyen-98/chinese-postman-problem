
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
odd_degree_list = get_odd_degree_list(G)

len_od_list = len(odd_degree_list)

def pairing_vertex(od_list, ret_list, singular_ord):
    global len_od_list
    
    i = 0
    while i < len_od_list and od_list[i] == "_":
        i+=1
    
    if i >= len_od_list:
        ret_list.append([])
        ret_list[-1] = [sublist.copy() for sublist in singular_ord]
              
    else:
        singular_ord.append([od_list[i]])
        od_list[i] = "_"
        for j in range(i+1, len_od_list):
            if od_list[j] != "_":
                singular_ord[-1].append(od_list[j])
                od_list[j] = "_"
                pairing_vertex(od_list, ret_list, singular_ord)
                
                od_list[j] = singular_ord[-1][-1]
                del singular_ord[-1][-1]
                
        od_list[i] = singular_ord[-1][0]
        del singular_ord[-1]
    
    return ret_list
        
print(pairing_vertex(odd_degree_list, [], []))
        
    



