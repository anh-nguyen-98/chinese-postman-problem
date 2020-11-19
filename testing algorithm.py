"""
first algorithm test
author:
"""
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

filename = "graph 1.csv"
with open(filename, 'r') as in_file:
    data = pd.read_csv(filename)
    
G = nx.Graph()
G.add_nodes_from(data.columns[1:])
print(G.nodes)


for row in data.index.array:
    for col in data.columns[1:]:
        data = data.fillna(0)
        if data.iloc[row][col] != 0:
            G.add_edge(data.iloc[row][0], col, weight = data.iloc[row][col])
   
            
#print(data.iloc[0]['B'])           
print(G.edges)

pos = nx.spring_layout(G)  # positions for all nodes

print (pos)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
plt.axis("off")
plt.show()