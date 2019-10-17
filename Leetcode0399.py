class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build a table to store x/y and y/x
        table = collections.defaultdict(dict)
        for i in range(len(equations)):
            (x, y), val = equations[i], values[i]
            table[x][y] = val
            table[y][x] = 1.0/val
        print table
        # traverse the graph using dfs
        res = []
        for query in queries:
            visited = set()
            a, b = query
            res.append(self.dfs(a, b, table, visited))
        return res
        
    def dfs(self, x, y, table, visited):
        if x not in table or y not in table:
            print x, y, "case1"
            return -1.0
        if x == y:
            return 1.0
        if y in table[x]:
            return table[x][y]
        if x in table[y]:
            return 1.0/table[y][x]
        visited.add(x)
        for a in table[x].keys():
            # print x, a
            if a in visited:
                continue
            print "now traverse", a, y
            res = self.dfs(a, y, table, visited) 
            if  res != -1:
                return table[x][a] * res
        print x, y, "case2"
        return -1.0
