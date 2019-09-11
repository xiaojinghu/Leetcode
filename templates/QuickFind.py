class QuickFind(object):

    def __init__(self, n):
        """
        parameters: 
            n: number of elments
        """
        self.root = list(range(n))

    def union(self, x, y):
        """
        union cluter x with cluster y
        """
        rootX = self.root[x]
        rootY = self.root[y]

        # we need to set root[k]= rootX for all k having root[k] == rootY
        for k in range(len(root)):
            if self.root[k] == rootY:
                root[k] = rootX

    def find(self, x, y):
        return self.root[x] == self.root[y]

    

