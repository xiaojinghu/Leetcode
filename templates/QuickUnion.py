# This is the lasy approach implementation of quick find

class QuickUnion(object):

    def __init__(self, n):
        self.parent =  list(range(n))

    def getRoot(self, x):
        while(self.parent[x]!=x):
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        root[rootX] = rootY

    def find(self, x, y):
        return self.getRoot(x)==self.getRoot(y)

        

