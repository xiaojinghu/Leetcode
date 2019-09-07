class Solution(object):
    def findRoot(self, parents, x):
        # return root of x
        List = []
        # find root
        while(parents[x]!=x):
            List.append(x)
            x = parents[x]
        # flattening
        for i in List:
            parents[i] = x
        return x
    
    def union(self, parents, x, y):
        parent_x = self.findRoot(parents, x)
        parent_y = self.findRoot(parents, y)
        if parent_x != parent_y:
            parents[parent_y] = x
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # for a tree, len(edges) == n-1
        if len(edges) != n-1:
            return False
        
        # originally, we initialize the parent of each node to be it self, i.e., each node is isolated
        parents = [i for i in range(n)]
        for x ,y in edges:
            # x and y should be connected, i.e, they should have the same parent
            # if x and y has the same parent, then the parent of x, x, and y are already on a path, if we connect the parent of x and y, there must be a cycle
            if self.findRoot(parents, x) == self.findRoot(parents, y):
                return False
            self.union(parents, x, y)
        # if it is a tree, then we shall have only one root 
        # find the root node for each node
        for i in range(1, n):
            if self.findRoot(parents, i)!=self.findRoot(parents, i-1):
                return False
        return True
        
        