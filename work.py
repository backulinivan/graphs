import matplotlib.pyplot as plt
import networkx as nx

def read_graph():
    G = nx.Graph()
    l = file.readlines()
    for r in l:
        r = r.split()
        G.add_edge(r[0], r[1])
    return G

def graph_to_dict(G):
    nodes = [int(x) for x in G.nodes()]
    neighbours = []
    for i in nodes:
        neighbours.append([int(x) for x in G.neighbors(str(i))])
    l = {node: set(attached) for node, attached in zip(nodes, neighbours)}
    return l

def dfs(G, start, called):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            dfs(G, neighbour, called)
            return called

file = open('graph.txt', 'r')


graph = read_graph()
pos = nx.spring_layout(graph)
print(graph_to_dict(graph))
print(dfs(graph_to_dict(graph), 0, set()))

nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
nx.draw_networkx_labels(graph, pos, font_size=12)
plt.savefig('graph.png')



plt.show()

