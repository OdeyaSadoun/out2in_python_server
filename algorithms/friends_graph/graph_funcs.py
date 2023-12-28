from matplotlib import pyplot as plt
import networkx as nx
import numpy as np

friends_list = [{"student": 1, "friends": [2,3,4]},{"student": 2, "friends": [5,3,4]},{"student": 5, "friends": [2,3,4]},{"student": 4, "friends": [2,5,1]}]

def make_directed_graph_for_connections_between_students(friends_list):
    g = nx.DiGraph()

    for student in friends_list:
        g.add_node(student["student"])
        for friend in student["friends"]:
            g.add_edge(student["student"], friend)

    # הדפסת הגרף בתצוגה ויזואלית
    nx.draw(g, with_labels=True)
    plt.show()
    return g


def out_degree(g, node):
    return len(list(g.neighbors(node)))


def in_degree(g, node):
    edges = list(g.edges)
    return sum([1 for edge in edges if edge[1] == node])


def normalize(degree):
    if degree == 0:
        return 0
    return degree / max(degree)


def statistic(vertex, g, degrees_in, degrees_out):

    # 1:
    din = in_degree(g, vertex)
    din = din / max(degrees_in)

    # 2:
    dout = out_degree(g, vertex)
    dout = dout / max(degrees_out)

    # 3:
    # degree = din + dout
    pre = g.predecessors(vertex)
    suc = g.successors(vertex)
    count = 0
    for item in suc:
        if item in pre:
            count = count + 1
    count = count / max(max(degrees_in), max(degrees_out))

    final = round(1 / 3 * din + 1 / 3 * dout + 1 / 3 * count, 1)

    return final


def scanGraph(g):
    d = {}
    print(list(g))
    for node in list(g):
        d[node] = (in_degree(g, node), out_degree(g, node))
        # print(node, in_degree2(g,node),out_degree(g,node))
    return d

def create_degrees(d):
    degrees_in = []
    degrees_out = [] 
    for vertex, (in_degree, out_degree) in d.items():
        degrees_in.append(in_degree)
        degrees_out.append(out_degree)
    return degrees_in, degrees_out


def calc_social_index_students(friends_list):
    print("enter py func")
    friends_array = np.array(friends_list)
    g = make_directed_graph_for_connections_between_students(friends_array)

    d = scanGraph(g)
    print("d", d)
    degrees_in, degrees_out = create_degrees(d)

    print(degrees_in, degrees_out)

    d_statistic = {}

    for key in d:
        mark = statistic(key, g, degrees_in, degrees_out)
        for node in list(g):
            if node == key:
                d_statistic[node] = mark
     
    print(d_statistic)
    return d_statistic


