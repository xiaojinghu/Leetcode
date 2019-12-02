class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        #idea:将所有树的高度排序。每次取出高度最低的一棵树，算出当前出发点离该树的最短距离， 直到所有树都被取出。
        #tree可以walk through :)
        # get a list of trees and their positions
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1:
                    trees.append((forest[i][j], i, j))
        #sort the trees in descending order
        trees.sort(reverse = True)
        # Now we need to do BFS for each starting node.
        minStep = 0
        # currently the starting point is (0,0)
        queue = collections.deque([[0,0,0]])
        while(trees):
            # get the next tree to be cutted
            nextHeight, next_i, next_j = trees.pop()
            visited = set()
            pathDist = float('inf')
            while(queue):
                currDist, curr_i, curr_j = queue.pop()
                if curr_i == next_i and curr_j == next_j:
                    # cut the tree
                    forest[curr_i][curr_j] = 1
                    #update pathDist
                    pathDist = currDist
                    #update queue
                    queue = collections.deque([])
                    break
                # if we've visited this position, move on
                if (curr_i, curr_j) in visited:
                        continue
                # mark the current position as visited
                visited.add((curr_i, curr_j))
                # visit its neighbors
                for (m, n) in [(curr_i-1, curr_j), (curr_i+1, curr_j), (curr_i, curr_j-1), (curr_i, curr_j+1)]:
                    if 0<=m<len(forest) and 0<=n<len(forest[0]) and (m,n) not in visited and forest[m][n]!=0:
                        if forest[m][n]!=0:
                            queue.appendleft([currDist+1, m, n])
            
            if pathDist == float('inf'):
                return -1
            # print pathDist
            minStep += pathDist
            # update queue
            queue.appendleft([0, next_i, next_j])
        return minStep
                                
                    
            
            
        
        