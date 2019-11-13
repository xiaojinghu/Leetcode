class Solution(object):
    #Rejection Sampling.这其实就是拒绝采样的经典应用，在一个正方形中有均匀分布的点，随机出其内切圆中的一个点，那么就是随机出x和y之后，然后算其平方和，如果小于等于r平方，说明其在圆内，可以返回其坐标，记得加上圆心偏移，否则重新进行采样。

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.xCenter = x_center
        self.yCenter = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # generate a random point 
        x = random.uniform(self.xCenter-self.radius, self.xCenter+self.radius)
        y = random.uniform(self.yCenter-self.radius, self.yCenter+self.radius)
        if (x-self.xCenter)**2+(y-self.yCenter)**2<self.radius**2:
            return [x,y]
        else:
            return self.randPoint()
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()