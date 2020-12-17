"""
The module deals with odd-degree vertex list retrieve and pairing.

author: Nguyen Ba Hoc, Nguyen Hoang Nam Anh
"""
import graph


"""
Param: (Nx. Multigraph) G

Returns list of odd-degree vertex
"""


def get_odd_degree_list(G):
    odd_degree_list = []
    # degree_list = [val for (node, val) in G.degree()]
    for i in G.degree():
        if i[1] % 2 == 1:
            odd_degree_list.append(i[0])
    return odd_degree_list

"""
Param:  (ls) od_list: list of all odd-degree vertices
        (ls) ret_list: list of all possible pairings (combinations) of odd-degree vertices 
        (ls) singular_ord: being-built pairing (combination) 
        (int) len_od_list: length odd-degree vertice list 
                
returns (ls) list of all possible pairings (combinations) of odd-degree vertices
"""


def pairing_vertex(od_list, ret_list, singular_ord, len_od_list):

    i = 0
    while i < len_od_list and od_list[i] == "_":
        i += 1

    if i >= len_od_list:
        ret_list.append([])
        ret_list[-1] = [sublist.copy() for sublist in singular_ord]

    else:
        singular_ord.append([od_list[i]])
        od_list[i] = "_"
        for j in range(i + 1, len_od_list):
            if od_list[j] != "_":
                singular_ord[-1].append(od_list[j])
                od_list[j] = "_"
                pairing_vertex(od_list, ret_list, singular_ord, len_od_list)

                od_list[j] = singular_ord[-1][-1]
                del singular_ord[-1][-1]

        od_list[i] = singular_ord[-1][0]
        del singular_ord[-1]

    return ret_list


