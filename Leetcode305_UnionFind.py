class QuickUnion(object):
    def __init__(self, objectList):
        self.parent = {}
        self.size ={}
        for i in range(len(objectList)):
            self.parent[objectList[i]] = objectList[i]
            self.size[objectList[i]] = 1
        
    def getRoot(self, x):
        while(x!=self.parent[x]):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if self.size[rootX]<=self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            return
        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        return 
    
    def find(self, x, y):
        return self.getRoot(x)==self.getRoot(y)

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # firstly transfer positions into tuples so that they can be used as keys
        positions = map(tuple, positions)
        # print positions
        quickunion = QuickUnion(positions)
        # print quickunion.parent
        res = []
        islands = set()
        for i in range(len(positions)):
            index_i, index_j = positions[i]
            if positions[i] in islands:
                res.append(res[-1])
                continue
            neighbours = []
            for p,q in [(index_i-1, index_j), (index_i, index_j-1), (index_i+1, index_j), (index_i, index_j+1)]:
                if 0<=p<m and 0<=q<n and (p,q) in islands:
                    neighbours.append((p,q))
            prevCount = len(set(map(quickunion.getRoot, neighbours)))
            for neighbour in neighbours:
                quickunion.union(neighbour,(index_i, index_j))
            currCount = len(set(map(quickunion.getRoot, neighbours+[(index_i, index_j)])))
            # print prevCount, currCount
            islands.add((index_i, index_j))
            if not res:
                res.append(currCount)
            else:
                res.append(res[-1]+currCount-prevCount)
                
            
        return res