class UnionFind(object):
    def __init__(self, n):
        self.parent = range(n)
        self.size = [1]*n
    
    def getRoot(self,x):
        while(x!=self.parent[x]):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX == rootY:
            return 
        if self.size[rootX]>=self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            return
        self.parent[rootX] = rootY
        self.size[rootY] += self.size[rootX]
        
    def find(self, x,y):
        return self.getRoot(x) == self.getRoot(y)
    
    
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        # for every connected component, if there is two or more infected nodes, remove one node won't reduce the number of infected nodes in this component. So we just need to consider the connected componnent with one infected node and choose the biggest one.
        
        # initialize the unionfind instance
        unionfind = UnionFind(len(graph))
        
        # start clustering
        for u in range(len(graph)):
            for v in range(len(graph)):
                if u == v:
                    continue
                if graph[u][v] == 1:
                    unionfind.union(u,v)
        
        # set an map to count the infected nodes for each cluster
        count = {}
        for infectedNode in initial:
            root = unionfind.getRoot(infectedNode)
            if root not in count:
                count[root] = []
            count[root].append(infectedNode)
        #choose 
        maxSize = 0
        index = -1
        for root in count:
            if len(count[root])>=2:
                continue
            rmNode = count[root][0]
            if unionfind.size[root]>maxSize:
                maxSize = unionfind.size[root]
                index = rmNode
                continue
            if unionfind.size[root] == maxSize:
                if rmNode<index:
                    index = rmNode
 
        if index == -1:
            return min(initial)
        return index
            
