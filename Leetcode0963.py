class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        #idea: 我们穷举任意的一对点（记作点i和点j），那么ij所组成的一条线段，可以用deltaX = xj-xi, deltaY = yj-ji来表示它的方向和长度。
        #我们将同属于{deltaX,deltaY}的point pair（或者说线段）放在一起，即 Map[{deltaX,deltaY}].push_back({i,j}); 那么对于同一个key = {deltaX,deltaY}所代表的这些线段，两两之间都一定可以组成一个平行四边形！
        #我们遍历这些平行四边形。对于每一个平行四边形，它们的四个点的坐标都是已知的（比如记作ijkt）。我们可以通过考察向量ij和向量jk是否垂直来判定这个四边形是否是矩形。数学上，具体的做法是考察两个二维向量的点积是否为零。即v1(x1,y1)垂直于v2(x2,y2) <=> x1*x2+y1*y2 = 0。如果确认是矩形，那我们很容易计算它的面积，记录下来求最小值即可。
        #这种做法的效率较高，原因是我们将所有的线段（N^2)条按照“长度+方向”进行了分类。每一类里的线段数目其实比较少，做两两组合（构建平行四边形）的开销不大。
        hashMap = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # choose two distinct points to form a vector
                # print i, j, points[i], points[j]
                point1 = points[i]
                point2 = points[j]
            #To avoid the same line segments to be represented in different ways ， we set deltaX>=0
                deltaX = point2[0]-point1[0]
                deltaY = point2[1]-point1[1]
                if deltaX == 0 and deltaY == 0:
                    # make sure the two points are distinct
                    continue
                if deltaX<0:
                    deltaX = -deltaX
                    deltaY = -deltaY
                    point1, point2  = point2, point1
                if (deltaX, deltaY) not in hashMap:
                    hashMap[(deltaX, deltaY)] = []
                hashMap[(deltaX, deltaY)].append([point1, point2])    
        # for every two distinct pairs of points in the hashMap, they must can form a paralelogram, we just need to check if this parallelogram is a rectangle. And if it is, we update the minimum area.
        minArea = float('inf')
        for (deltaX, deltaY) in hashMap:
            pointsList = hashMap[(deltaX, deltaY)]
            for i in range(len(pointsList)):
                for j in range(i+1, len(pointsList)):
                    left1, right1 = pointsList[i]
                    left2, right2 = pointsList[j]
                    lenVec = [deltaX, deltaY]
                    widVec = [left2[0]-left1[0], left2[1]-left1[1]]
                    if (deltaX==0 and deltaY==0) or (widVec[0]==0 and widVec[1]==0):
                        #make sure none of the two vectors is a zero-vec
                        continue
                    # check if we can get a rectangle
                    if lenVec[0]*widVec[0]+lenVec[1]*widVec[1]==0:
                        # update the area
                        length = (deltaX**2+deltaY**2)**0.5
                        width = (widVec[0]**2+widVec[1]**2)**0.5
                        print length, width
                        minArea = min(minArea, length*width)
        if minArea == float('inf'):
            return 0
        return minArea