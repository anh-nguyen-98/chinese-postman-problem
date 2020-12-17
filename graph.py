"""

"""
import networkx as nx
import pandas as pd
import turtle
import matplotlib.pyplot as plt
from visualize_graph import track_route


def retrieve_graph(filename):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    G = nx.MultiGraph()
    G.add_nodes_from(data.columns[1:])

    for row in data.index.array:
        for col in data.columns[row+1:]:
            #data = data.fillna(0)
            if data.iloc[row][col] != 0:
                G.add_edge(data.iloc[row][0], col, weight=data.iloc[row][col])
    # positions for all nodes
    
    pos = nx.spring_layout(G)
    
    # nodes
#     nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
#     nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
    nx.draw(G, with_labels = True)
    plt.axis("off")
    plt.savefig("our_graph.png")
#     plt.show()
    return G

retrieve_graph('graph 1.csv')