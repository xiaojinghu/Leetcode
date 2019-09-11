# Solution to the single shortest path problem
# all edges must have non-negtive weights
# graph must be connected

def (graph, s):
    # return the distance of the shortest path from source s to all other vertices 
    # v in the graph
    # the distances are represented using a map
    dist = {}
    # the diastance from source to source is initialized as 0
    dist[s] = 0
    # the distance from source to all other nodes is infinity
    for v in graph.vertices-[s]:
        dist[v] = float('inf')
    
    # constain all vertices in a queue
    queue = collections.deque([graph.vertices])

    while(queue):
         # select the vertex that has the minimum distances from s
         # initially it is s, then s's neighbours, then s's decendents
         u = minVertex(queue)
         # mark u as visited， which means its shortest path is found
         for v in graph[u]:
            if v in visited:
                continue
            # if we find an shortest path
            if dist[v]>dist[u]+weight[u][v]:
                dist[v] = dist[u]+weight[u][v]
                queue.append(v)

    return dist


