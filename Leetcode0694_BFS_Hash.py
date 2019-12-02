class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        landSet = set()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # this is a new land
                    queue = collections.deque([(i,j)])
                    # path is to store the ralative positions of the 1s
                    path = []
                    while(queue):
                        p, q = queue.pop()
                        if (p, q)in visited:
                            continue
                        visited.add((p, q))
                        path.append(p-i)
                        path.append(q-j)
                        for (m,n) in [(p-1, q), (p+1, q), (p, q-1), (p, q+1)]:
                            if 0<=m<len(grid) and 0<=n<len(grid[0]) and (m, n) not in visited and grid[m][n] == 1:
                                queue.appendleft((m,n))
                    path = tuple(path)
                    # print path
                    if path not in landSet:
                        landSet.add(path)
        return len(landSet)