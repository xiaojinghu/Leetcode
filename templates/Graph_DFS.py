# key idea: strat at one vertex, and visit its first neighbor first.


def DFS_visit(graph, u, color):
    # we mark the current node as discovered
    color[u] = "grey"

    for v in graph[u]:
        if color[v] == "white":
            DFS_visit(v)
    color[u] = "black"

