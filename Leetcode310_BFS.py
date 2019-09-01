class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        # build the graph using map
        graph = collections.defaultdict(set)
        for (k, v) in edges:
            graph[k].add(v)
            graph[v].add(k)
        # The method is to delete leaves level by level, then the one or two nodes remaining are roots of minimum height trees.
        queue = collections.deque()
        # initialize the queue
        for (u,vs) in graph.items():
            if len(vs) == 1:
                # This means u is a leaf node
                # we push it into the queue
                queue.appendleft(u)
                
        while(n>2):
            # Note here we must delete all leaf nodes at a time
            # since they are on the same level
            queueLen = len(queue)
            for i in range(queueLen):
                u = queue.pop()
                for v in graph[u]:
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        queue.appendleft(v)
            n -= queueLen
        return queue