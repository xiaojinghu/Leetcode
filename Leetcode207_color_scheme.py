from collections import deque
class Solution(object):  
    def dfs(self, u, color, graph):
        # we traverse its neighbors
        for v in graph[u]:
            if color[v] == "black":
                continue
            if color[v] == "grey":
                return False
            if color[v] == "white":
                color[v] = "grey"
                if self.dfs(v, color, graph):
                    continue
                else:
                    return False
        color[u] = "black"
        return True
                
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # we can use DFS to solve this problem
        # first, build the adjacancy list and the in-degree array
        graph = {}
        for edge in prerequisites:
            u = edge[1]
            v = edge[0]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
        
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
            if not self.dfs(s, color, graph):
                return False
        return True