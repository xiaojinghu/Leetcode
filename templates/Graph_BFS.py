# Goal: always visit adjacent nodes first
# Color scheme:
    # white: a newly discovered node
    # gray: a discovered node which has not been completely processed
    # black: a completely processed node

def BFS(graph, s):
    # Initializtion: mark all nodes as white
    for vertex in graph.vertice:
        color[vertex] = "white"

    # mark source node as grey
    # we push gray nodes onto the queue
    queue = deque([s])
    while(queue):
        # pop the current node
        currVertex = queue.pop()
        # Access its neighbors
        for neighbor in currVetex.neighbors:
            # if it is white, we  mark it as gray and push it into the queue
            if color[neighbor] == "white":
                color[neighbor] = "gray"
                queue.appendleft(neighbor)
        # after enqueuing all neighbors of currVertex, we mark current vertex as processed
        color[currVertex] = "black"

# Actually, when we are traversing a graph, we usually do not need a "grey" status because
# we just need to check whether it is white or not.
# so we can have a visited set instead.
def BFS(graph, s):
    # Initializtion
    # All nodes in visited are "black" or "gray"
    # All nodes not in visited are "white"
    visited = {}

    # mark source node as grey
    visited.add(s)
    # we push gray nodes onto the queue
    queue = deque([s])
    while(queue):
        # pop the current node
        currVertex = queue.pop()
        # Access its neighbors
        for neighbor in currVetex.neighbors:
            # if it is white, we  mark it as gray and push it into the queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft(neighbor)
        # after enqueuing all neighbors of currVertex, we mark current vertex as processed
        