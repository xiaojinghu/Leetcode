class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #本题可以解读为，从左上角到右下角，找出两条可行的线路，使得两条线路采集到的cherry数量最多．如果两条线路有重复的部分，则只算一次．
       #如果只有一条线路，那很明显用dp算法，每一个点的状态仅仅取决于它左边和上边两个点，转移方程为dp[i][j]＝max{dp[i-1][j],dp[i][j-1]}+grid[i][j]．
       #那么对于两条线路，我们需要同时考虑两个点的状态。假设有两个人同时采樱桃， 其中在同一地点的樱桃只能被同一个人采完。 假设这两个人停下来的位置为(i1, j1), (i2, j2)，此时他们一共采到的樱桃的最大个数为dp[i1][j1][i2][j2]，那么我们知道， (i1, j1)先前可能的位置为(i1-1, j1)和(i1, j1-1),(i2, j2)先前的位置为(i2-1, j2), (i2, j2-1),那么两个人先前的位置共有4种可能组合，我们应该从中挑选摘取樱桃最多的组合。由于两个人是同时出发，所以i1+j1 = i2+j2， 所以实际上dp为3维。
        dp = []
        n = len(grid)
        # Initialization of dp
        for i in range(n):
            dp.append([])
        for i in range(n):
            for j in range(n):
                # Initially we mark each position as unreachable
                dp[i].append([-1]*n)
                
        #Start looping
        for i1 in range(n):
            for j1 in range(n):
                for i2 in range(n):
                    j2 = i1+j1-i2
                    # check the vadality of both positions
                    if j2<0 or j2>=n or grid[i1][j1]==-1 or grid[i2][j2]==-1:
                        continue
                    valid1 = []
                    valid2 = []
                    if i1-1>=0:
                        valid1.append([i1-1, j1])
                    if j1-1>=0:
                        valid1.append([i1, j1-1])
                    if i2-1>=0:
                        valid2.append([i2-1, j2])
                    if j2-1>=0:
                        valid2.append([i2, j2-1])

                    maxCount = float('-inf')
                    for m1, n1 in valid1:
                        for m2, n2 in valid2:
                            maxCount = max(maxCount, dp[m1][n1][m2])
                    # case1, no way to reach i1, j1, i2, j2
                    if maxCount == -1:
                        continue
                    # case2, there is a way to reach i1,j1, i2, j2 or it is at the boundry
                    maxCount = max(0, maxCount)
                    if grid[i1][j1]+grid[i2][j2] <= 1:
                        dp[i1][j1][i2] = grid[i1][j1]+grid[i2][j2]+maxCount
                        continue
                    
                    if grid[i1][j1]+grid[i2][j2] == 2:
                        if i1==i2:
                            dp[i1][j1][i2] = 1+maxCount
                        else:
                            dp[i1][j1][i2] = 2+maxCount    
        return max(0, dp[n-1][n-1][n-1])