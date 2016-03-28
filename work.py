import matplotlib.pyplot as plt
import networkx as nx

def read_graph():
    G = nx.Graph()
    l = file.readlines()
    for r in l:
        r = r.split()
        if len(r) == 1:
            G.add_node(r[0])
        elif len(r) == 2:
            G.add_edge(r[0], r[1])
        elif len(r) == 3:
            G.add_edge(r[0], r[1], length = float(r[2]))
        else: pass

    return G

def dfs(G, start, called = set(), dfs_result = nx.Graph()):
    called.add(str(start))
    for neighbour in G[str(start)]:
        if neighbour not in called:
            dfs(G, neighbour, called)
            dfs_result.add_edge(str(start), neighbour, length = G[str(start)][neighbour].get('length'))
    return dfs_result

def bfs(G, start, fired = set(), bfs_result = nx.Graph()):
    fired.add(str(start))
    queue = [str(start)]
    while len(queue) != 0:
        current = queue.pop(0)
        for neigbour in G[current]:
            if neigbour not in fired:
                fired.add(neigbour)
                queue.append(neigbour)
                bfs_result.add_edge(neigbour, current, length = G[current][neigbour].get('length'))
    return bfs_result

def dijkstra(G, start):
    shortest_paths = {node:float('+inf') for node in G}
    shortest_paths[str(start)] = 0
    queue = [str(start)]
    shortest_from = [-1]*len(nx.nodes(G))
    while len(queue) != 0:
        current = queue.pop(0)
        for neighbour in G[current]:
            offered_path = shortest_paths[current] + G[current][neighbour]['length']
            if offered_path < shortest_paths[neighbour]:
                shortest_paths[neighbour] = offered_path
                queue.append(neighbour)
                shortest_from[int(neighbour)] = current
    return (shortest_paths, shortest_from)

def shortest_one_another(G, node1, node2):
    shortest_from = dijkstra(G, node1)[1]
    path = []
    while shortest_from[int(node2)] != -1:
        path.append((node2, shortest_from[int(node2)]))
        node2 = shortest_from[int(node2)]
    return path

def draw_graph(G, pos, name = 'graph.png', color = 'black'):
    lbl = {}
    for x in G:
        for y in G[x]:
            lbl[(x, y)] = G[x][y].get('length')
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color= color)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=lbl)

    plt.savefig(name)


file = open('graph.txt', 'r')

print('Enter the start node:', end=' ')
str_node = input()

graph = read_graph()
position = nx.spring_layout(graph)
depth = dfs(graph, str_node)
breadth = bfs(graph, str_node)
optimal_paths = dijkstra(graph, str_node)[0]

print('Shortest paths from ' + str_node + ':')
for node in graph:
    print(node, optimal_paths[node])

print('Enter two nodes:', end=' ')
nds = input().split()
highlight = shortest_one_another(graph, nds[0], nds[1])

#print(shortest_path(graph, '2', '4'))

file.close()

plt.subplot(1, 3, 1)
plt.title('Graph')
draw_graph(graph, position)
nx.draw_networkx_edges(graph, position, highlight, edge_color='green', alpha=0.5, width=4.0)
plt.subplot(1, 3, 2)
plt.title('DFS result from ' + str_node)
draw_graph(depth, position, 'dfs_graph.png', color='red')
plt.subplot(1, 3, 3)
plt.title('BFS result from ' + str_node)
draw_graph(breadth, position, 'bfs_graph.png', color='blue')

plt.show()