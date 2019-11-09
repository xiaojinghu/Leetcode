class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Do BFS for each empty room
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                # if this is a gate,we add it into the queue
                if rooms[i][j] == 0:
                    queue.appendleft((i,j))
        while(queue):
            size = len(queue)
            for index in range(size):
                i, j = queue.pop()
                for m, n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=m<len(rooms) and 0<=n<len(rooms[0]) and rooms[m][n]>rooms[i][j]+1:
                        rooms[m][n] = rooms[i][j]+1
                        queue.appendleft((m,n))
        
