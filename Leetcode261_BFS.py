class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {i:set() for i in range(n)}
        # build the undirected graph
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        visited = set()
        queue = collections.deque([0])
        while(queue):
            currNode = queue.pop()
            # if current node is visited, this means there is a cycle
            if currNode in visited:
                return False
            # we mark the current node as visited
            visited.add(currNode)
            for neighbour in graph[currNode]:
                queue.appendleft(neighbour)
                # we remove the edge from its neighbour to current node to avoid repeated visiting
                graph[neighbour].remove(currNode)
        return len(visited) == n
            
        
        
            
        
        