class Solution(object):
    def getRoot(self, x):
        while(self.parent[x] != x):
            # path compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            # we append the x cluster to y
            self.parent[rootX] = rootY
            return 
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            return
        
        self.parent[rootX] = rootY
        self.rank[rootY] += 1
    
    def isSimilar(self, A, B):
        """
        return True if A and B are similar
        """
        if len(A)!=len(B):
            return False
        diffCount = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            diffCount += 1
            if diffCount>2:
                return False
        if diffCount == 0 or diffCount == 2:
            return True
        return False
    
    
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = list(set(A))
        self.parent = range(len(A))
        self.rank = [0]*len(A)
       
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if self.isSimilar(A[i],A[j]):
                    self.union(i,j)
        
        rootSet = set()
        for i in range(len(A)):
            rootSet.add(self.getRoot(i))
        return len(rootSet)
