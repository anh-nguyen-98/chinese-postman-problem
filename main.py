"""
Discrete math final project
author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import check_eulerian
import graph

from graph_shortest_path.shortest_pairing import find_shortest_path
from graph_shortest_path.shortest_pairing import find_shortest_distance
from graph_shortest_path.shortest_pairing import previous_vertex
from graph_shortest_path.odd_degree_pairing import get_odd_degree_list, pairing_vertex
from graph_shortest_path.shortest_pairing import find_shortest_pairing

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
        print(G.edges.data())
    else:
        print(G.edges.data())

    # visualize_graph


main()
