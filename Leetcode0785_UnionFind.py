class QuickUnion(object):
    def __init__(self, N):
        self.parent = range(N)
        self.size = [1]*N
    
    def getRoot(self, x):
        while(x!=self.parent[x]):
            self.parent[x] = self.parent[self.parent[x]]
            x= self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if self.size[rootX]<=self.size[rootY]:
            self.parent[rootX]= rootY
            self.size[rootY] += self.size[rootX]
            return 
        self.parent[rootY]= rootX
        self.size[rootX] += self.size[rootY]
        return 
    
    def find(self, x, y):
        return self.getRoot(x) == self.getRoot(y)


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        quickunion = QuickUnion(len(graph))
        for i in range(len(graph)):
            if not graph[i]:
                continue
            node = graph[i][0]
            for j in graph[i]:
                #check if i and j are in the same cluster
                if quickunion.find(i,j):
                    return False
                # connect all its neighbours
                if not quickunion.find(node, j):
                    quickunion.union(node, j)
        return True
                
