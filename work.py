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

def dfs(G, start, called = set(), fired_edges = []):
    called.add(start)
    for neighbour in G[start]:
        print(1)
        if neighbour not in called:
            fired_edges.append((str(start), str(neighbour)))
            fired_edges.append((str(neighbour), str(start)))
            dfs(G, neighbour, called)
    return fired_edges


file = open('graph.txt', 'r')


graph = read_graph()
pos = nx.spring_layout(graph)
print(graph_to_dict(graph))
fired = dfs(graph_to_dict(graph), 0)

nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos, [edge for edge in nx.edges(graph) if edge in fired], edge_color='red', width=4.0, alpha=0.5)
nx.draw_networkx_edges(graph, pos)
nx.draw_networkx_labels(graph, pos, font_size=12)
plt.savefig('graph.png')



plt.show()

