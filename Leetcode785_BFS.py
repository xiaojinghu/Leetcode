class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """  
        for node in range(len(graph)):
            setA = set()
            setB = set()
            visited = set()
            currSet = 'A'
            queue = collections.deque([node])
            while(queue):
                size = len(queue)
                for i in range(size):
                    currNode = queue.pop()
                    if currNode in visited:
                        continue
                    visited.add(currNode)
                    # add current node to current set and check conflicts
                    if currSet == 'A':
                        setA.add(currNode)
                        if currNode in setB:
                            return False
                    if currSet == 'B':
                        setB.add(currNode)
                        if currNode in setA:
                            return False
                    for neighbour in graph[currNode]:
                        if neighbour in visited:
                            if neighbour in setA and currNode in setA:
                                return False
                            if neighbour in setB and currNode in setB:
                                return False
                            continue
                        queue.appendleft(neighbour)
                if currSet == 'A':
                    currSet = 'B'
                else:
                    currSet = 'A'
            
        return True