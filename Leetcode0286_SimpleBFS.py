class Solution():    
    def wallsAndGates(self, rooms):
        """
        input: List[int][int]
        rtype: List[int][int]
        """
        # corner cases
        if not rooms or not rooms[0]:
            return rooms
        # initialize the queue
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.appendleft((i,j))
        # traverse the queue level by level
        # the level of the node is the shortest distance
        while(queue):
            row, col = queue.pop()
            # traverse its neighbors
            for m, n in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0<=m<len(rooms) and 0<=n<len(rooms[0]):
                    if rooms[m][n] == 2147483647:
                        rooms[m][n] = rooms[row][col]+1
                        queue.appendleft((m,n))
