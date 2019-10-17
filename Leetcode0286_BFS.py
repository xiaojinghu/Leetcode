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
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue = collections.deque([(i,j)])
                    while(queue):
                        row, col = queue.pop()
                        # traverse its neighbors
                        for m, n in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if 0<=m<len(rooms) and 0<=n<len(rooms[0]):
                                # the expected distance from the current path us currDis+1
                                if rooms[row][col]+1<rooms[m][n]:
                                    # current path is shorter, we see if we can update the neighbors of the neighbor
                                    # update the value of rooms[m][n]
                                    rooms[m][n] = rooms[row][col]+1
                                    queue.appendleft((m,n))
