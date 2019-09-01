from collections import deque
class Solution(object):           
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # we can use topological sorting to solve this problem
        # first, build the adjacancy list and the in-degree array
        graph = {}
        inDegree = {}
        for edge in prerequisites:
            u = edge[1]
            v = edge[0]
            if u not in inDegree:
                inDegree[u] = 0
            if v not in inDegree:
                inDegree[v] = 0
            inDegree[v] += 1
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
        # build a queue to store all edges that have zero in-degrees
        queue = deque()
        # push all vertice that has a zero in-degree into the queue    
        for vertex in inDegree:
            if inDegree[vertex] == 0:
                queue.append(vertex)
        # print inDegree, queue , graph     
        # start deleting vertice with zero in-degree
        while(queue):
            node = queue.popleft()
            # we mark the inDegree of this node as -1
            inDegree[node] = -1
            # deduct 1 from all nodes adjacant to it
            for neighbor in graph[node]:
                if inDegree[neighbor] == -1:
                    return False
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        # print inDegree    
        # after deleting, if there a re still nodes in the inDegree array, then there is cycle in the graph
        for vertex in inDegree:
            if inDegree[vertex] !=-1:
                return False
        return True
                    