class Solution(object):
    # idea: first a rectangle based on its area (randomly pick with weight), then pick a point randomly from this rectangle
    
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.range = [0]
        self.rects = rects
        for i in range(len(rects)):
            x1,y1,x2,y2 = rects[i]
            area = (x2-x1+1)*(y2-y1+1)
            self.range.append(self.range[-1]+area)
        
    def binarySearch(self, target):
        nums = self.range
        start = 0
        end = len(nums)-1
        while(start+1<end):
            # our goal is to narrow the range(start, end) while 
            # make sure nums[start]<=target<nums[end]
            middle = (start+end)/2
            if nums[middle]<=target:
                start = middle
            else:
                end = middle
        return start
        

    def pick(self):
        """
        :rtype: List[int]
        """
        randomInt = random.randint(0, self.range[-1]-1)
        randomRec = self.binarySearch(randomInt)
        x1,y1,x2,y2 = self.rects[randomRec]
        randomX = random.randint(x1,x2)
        randomY = random.randint(y1,y2)
        return (randomX,randomY)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()