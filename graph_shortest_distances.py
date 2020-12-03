from dijkstra import Graph
import pandas as pd

def find_shortest_distances (filename, G):
    with open(filename, 'r') as in_file:
        data = pd.read_csv(filename)

    list_of_rows = [list(row)[1:] for row in data.values]
    g = Graph(len(G.nodes))
    g.graph = list_of_rows
    distances = g.length_from_source()
    return distances