"""
Checks whether a graph is Eulerian.
author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""


def is_eulerian(G):
    degree_list = [val for (node, val) in G.degree()]
    for i in degree_list:
        if i % 2 == 1:
            return False
    return True
