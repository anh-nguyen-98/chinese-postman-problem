"""
Discrete math final project
author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import networkx as nx
import matplotlib.pyplot as plt
from pandas.core.indexes import multi
from networkx.drawing.nx_agraph import write_dot

import check_eulerian
import turtle
import graph
import  graphviz
import pydot
from networkx.drawing.nx_pydot import write_dot

from graph_shortest_path.shortest_pairing import find_shortest_path
from graph_shortest_path.shortest_pairing import find_shortest_distance
from graph_shortest_path.shortest_pairing import previous_vertex
from graph_shortest_path.odd_degree_pairing import get_odd_degree_list, pairing_vertex
from graph_shortest_path.shortest_pairing import find_shortest_pairing
# from visualize_graph import get_coordinates
from visualize_graph import track_route

"""
    Accomplishments so far:
        read csv file for graph data
        check if Eulerian
        draw graph on networkx
        length path
        odd degree list
        possible pairing between odd degree vertices
        Dijkstra
"""


def main():
    filename = "graph 1.csv"
    G = graph.retrieve_graph(filename)
    pos = nx.spring_layout(G)
    if not check_eulerian.is_eulerian(G):
        # odd-degree
        odd_degree_list = get_odd_degree_list(G)
        pairings = pairing_vertex(odd_degree_list, [], [], len(odd_degree_list))
        print("Pairings: ")
        print(pairings)

        distances = find_shortest_distance(filename, G)
        print("Shortest distances from each source node to other nodes: ")
        print(distances)

        # return id of shortest pairing in pairings
        shortest_pairing = find_shortest_pairing(G, pairings, distances)

        print("\nshortest pairing: ")
        print(pairings[shortest_pairing])
        
        path = find_shortest_path(filename, G)
        print(path)
        
        previous_vertices = previous_vertex(G, pairings, distances, filename)
        new_edges = []
        for i in range(len(previous_vertices)):
            new_edges = list(zip(previous_vertices[i], previous_vertices[i][1:]))
        print(new_edges)
        for edge in new_edges:
            if edge in G.edges:
                G.add_edge(edge[0], edge[1])
                G[edge[0]][edge[1]][1]['weight'] = G[edge[0]][edge[1]][0]['weight']

        visited = []
        coordinates = []
        route = track_route(G)
        for nodes in route:
            coordinates += [list(pos[nodes])]
        turtle.shape('turtle')
        turtle.penup()
        turtle.goto(coordinates[0][0]*300, coordinates[0][1]*300)
        for i in range(len(coordinates)):
            turtle.pendown()
            turtle.color('black')
            turtle.stamp()
            turtle.goto(coordinates[i][0]*300, coordinates[i][1]*300)
        
        for i in range(1, len(coordinates)):
            edge = list(zip(route[i], route[i-1]))
            if edge[0] in visited or edge[0][::-1] in visited:
                turtle.pendown()
                turtle.color('red')
                turtle.speed('slowest')
                turtle.stamp()
                turtle.pensize(3)
                turtle.goto(coordinates[i][0]*300, coordinates[i][1]*300)
            else:
                turtle.pendown()
                turtle.color('blue')
                turtle.speed('slowest')
                turtle.stamp()
                turtle.pensize(3)
                turtle.goto(coordinates[i][0]*300, coordinates[i][1]*300)
                visited += edge
        print(visited)      
        # # nodes
        # # nx.draw_networkx_nodes(G, pos, node_size=700)
        # # # edges
        # # nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
#         nx.draw(G, with_labels=True)
        # plt.axis("off")
        # plt.savefig("our_graph.png")
#         plt.show()
#         print(G.edges())

    else:
        print(G.edges.data())

    # visualize_graph

    
        

main()


