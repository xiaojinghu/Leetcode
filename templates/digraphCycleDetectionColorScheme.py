# key idea:
    # if a "grey" node has a "grey" descendent, then there is a cycle in the graph.


def dfs(self, u, color, graph):
    # node u has been discouvered and we've marked it as grey
    # we traverse its neighbors
    for v in graph[u]:
        if color[v] == "black":
            continue
        if color[v] == "grey":
            return True
        if color[v] == "white":
            color[v] = "grey"
            if self.dfs(v, color, graph):
                return True           
    color[u] = "black"
    return False



def cycle(graph):
        # we can use DFS to solve this problem
        # first, build the adjacancy list and the in-degree array
        # use color dict
        color = {}
        for vertex in graph.keys():
            color[vertex] = 'white'
         
        for s in graph.keys():
            # we select s as source and traverse the graph
            if s == "white":
                # we discover it and mark it as grey
                color[s] = "grey"
            # we traverse the graph from s
            if self.dfs(s, color, graph):
                return True
        return False
    