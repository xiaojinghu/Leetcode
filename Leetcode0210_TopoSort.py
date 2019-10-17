from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # THIS IS AN INDEGREE SOLUTION
        # build the indegree dict and the graph
        inDegree = {}
        graph = {}
        
        for course in prerequisites:
            start = course[1]
            end = course[0]
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
            if end not in graph:
                graph[end] = []
            if start not in inDegree:
                inDegree[start] = 0
            if end not in inDegree:
                inDegree[end] = 1
            else:
                inDegree[end] += 1
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
            if i not in inDegree:
                inDegree[i] = 0
                
                
        # build a queue
        queue = deque()
        # Initialization of the queue
        for course in inDegree.keys():
            if inDegree[course] == 0:
                queue.appendleft(course)
        
        res = []
        while(queue):
            node = queue.pop()
            # set this node as visited
            inDegree[node] = -1
            # add this node to the result
            res.append(node)
            
            # update the indegree of its neighbors and
            # check whether it can be added into the queue
            for neighbor in graph[node]:
                if inDegree[neighbor]==-1:
                    continue
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.appendleft(neighbor)
        
        for course in inDegree.keys():
            if inDegree[course]!=-1:
                return []
        
        return res
