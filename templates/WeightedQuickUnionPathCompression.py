class weightedQucikUnionPathCompression(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def getRoot(self, x):
        while(pself.arent[x] != x):
            # path compression
            self.parent[x] = self.parent[self.parent[x]]
        return x

    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX == rootY:
            return

        if self.size[rootX] <= self.size[rootY]:
            # we append the x cluster to y
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            return 

        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        return 

    def find(self, x, y):
        return self.getRoot(x)
        
