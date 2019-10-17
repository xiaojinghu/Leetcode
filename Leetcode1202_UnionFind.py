class UnionFind(object):
    def __init__(self,n):
        self.parent = range(n)
        self.size = [1]*n
        
    def getRoot(self,x):
        while(self.parent[x]!=x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX!=rootY:
            if self.size[rootX]>=self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
    def find(self, x,y):
        return self.getRoot(x)==self.getRoot(y)
    
    
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        if not s or not pairs:
            return s
        
        unionfind = UnionFind(len(s))
        for x,y in pairs:
            unionfind.union(x,y)
            
        # we put all indice that have the same root into a Map
        Map = {}
        for i in range(len(s)):
            root_i = unionfind.getRoot(i)
            if root_i not in Map:
                Map[root_i] = []
            Map[root_i].append(i)
        res = [0]*len(s)
        for root in Map:
            # we sort the set to get the order
            Map[root].sort()
            letters = [s[i] for i in Map[root]]
            letters.sort()
            for i in Map[root]:
                res[i] = letters[0]
                letters.pop(0)
        return ''.join(res)
                
            
        
