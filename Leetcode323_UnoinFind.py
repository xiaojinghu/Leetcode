class QuickUnion(object):
    def __init__(self, n):
        self.parent = range(n)
        self.size = [1]*n
        
    def getRoot(self, x):
        while(self.parent[x]!=x):
            # path compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if self.size[rootX] <= self.size[rootY]:
            self.parent[rootX]=rootY
            self.size[rootY] += self.size[rootX]
            return 
        self.parent[rootY]=rootX
        self.size[rootX] += self.size[rootY]
        return 
    
    def find(self, x, y):
        return self.getRoot(x) == self.getRoot(y)
    

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # THIS IS A WEIGHTED UNION FIND WITH PATH COMPRESSION  IMPLEMENTATION
        quickunion = QuickUnion(n)
        for edge in edges:
            x, y = edge
            quickunion.union(x, y)
        roots = set()    
        for i in range(n):
            roots.add(quickunion.getRoot(i))
        return len(roots)
        