class Solution():
    def dfs(self, i, j, rooms, dst):
        # termination conditions
        # case1: index out of bound
        if i<0 or i>=len(rooms) or j<0 or j>=len(rooms[0]):
            # out of bound
            return
        # case2, we've found an path which is shorter
        if rooms[i][j]<dst:
            return
        # set the current distance as dst
        rooms[i][j] = dst
        # traverse the nearby positions
        self.dfs(i-1, j, rooms, dst+1)
        self.dfs(i+1, j, rooms, dst+1)
        self.dfs(i, j-1, rooms, dst+1)
        self.dfs(i, j+1, rooms, dst+1)
    
    def wallsAndGates(self, rooms):
        """
        input: List[int][int]
        rtype: List[int][int]
        """
        # corner cases
        if not rooms or not rooms[0]:
            return rooms
        # we start traversing from each gate
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, rooms, 0)