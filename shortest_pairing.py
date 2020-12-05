"""

"""
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

