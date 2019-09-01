# Key idea:
       #Initialize and matain a queue(or stack) of vertices with indegreee 0


def topoSort(graph):
    # Initialize the indegree map
    inDegree = {}
    for u in graph.keys():
        vSet = graph[u]
         for v in vSet: 
            if v not in inDegree:
                inDegree[v] = 0 
            inDegree[v] += 1
        if u not in inDegree:
            inDegree[u] = 0


    # Initialize the queue
    queue = collections.deque()
    for v in inDegree.keys():
         # if the indegree for this vertex is 0, we push it into the queue
         if inDegree[v] == 0:
            queue.appendleft(v)

    # case 1, we did not find such a queue
    if len(graph) == 0:
        return False
    if not queue:
        return True

    while (queue):
        u = queue.pop()
        inDegree[u] = -1
        for v in graph[u]:
            if inDegree[v]==-1:
                # this means we meet a cycle
                return True
            inDegree[v] -= 1
            # update teh queue
            if inDegree[v] == 0:
                queue.appendleft(v)
     # after deleting, if there are still nodes in the inDegree array, then there is cycle in the graph
    for v in inDegree:
        if inDegree[vertex] != -1:
            return True
        return False

