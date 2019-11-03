class Solution(object):
    '''
    This is a PrefixSum and BinarySearch implementation.
    For weights = [1,2,3], we have weight[0] = 1, weight[1]=2, 
    weight[3] = 3, then we can assign a range for each number.
    For 0, it's [0,0+1=1); for 1 it's [1, 1+2=3) and for 3 it's
    [3, 3+3=6). When we need to randomly pick a number, we just need to generate a number randomly from range(sum(weights)), then find the range it's in and return the index of the range.
    '''
    def __init__(self, w):
        """
        :type w: List[int]
        """
        # generate the range list
        self.range = [0]
        for i in range(1, len(w)+1):
            self.range.append(self.range[-1]+w[i-1])
            
    def binarySearch(self, target):
        '''
        find the range target is in 
        '''
        nums = self.range
        start = 0
        end = len(self.range)-1
        while(start+1<end):
            # our goal is to keep nums[start]<=target<nums[end]
            middle = (start+end)/2
            if nums[middle]==target:
                start = middle
                continue
            if nums[middle]>target:
                end = middle
                continue
            if nums[middle]<target:
                start = middle
        return start
        # when it breaks, start+1=end, which is exacly the range size
        return start
                
            

    def pickIndex(self):
        """
        :rtype: int
        """
        randomInt = random.randint(0, self.range[-1]-1)
        return self.binarySearch(randomInt)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()