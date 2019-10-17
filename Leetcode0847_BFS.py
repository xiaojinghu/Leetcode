class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        # our final goal is to set all nodes as visited
        finalState = (1<<N)-1
        # print finalState
        # records the whole path length
        pathLen = 0
        # build a queue to visit the graph
        queue = collections.deque()
        for i in range(N):
            queue.append((i, 1<<i))
        visited = {}
        # initialize the visited states where the current node is i
        for i in range(N):
            visited[i] = set()
        
        while(queue):
            size = len(queue)
            for i in range(size):
                currNode, currState = queue.pop()
                # if we've visited all nodes, then we do not need to visit any more
                if currState == finalState:
                    return pathLen
                # if the current state is visited before, 
                # we skip this state( because we've recorded it in the queue)
                if currState in visited[currNode]:
                    continue
                visited[currNode].add(currState)
                for neighbour in graph[currNode]:
                    nextState = currState|(1<<neighbour)
                    queue.appendleft((neighbour, nextState))
            pathLen += 1
        return -1
