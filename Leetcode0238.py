class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        forward = []
        backward = collections.deque()
        res = []
        for i in range(len(nums)):
            if i == 0:
                forward.append(nums[i])
            else:
                forward.append(nums[i]*forward[i-1])
          
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                backward.appendleft(nums[i])
            else:
                backward.appendleft(nums[i]*backward[0])
        # print  forward, backward
        for i in range(len(nums)):
            if i == 0:
                res.append(backward[i+1])
                continue
            if i == len(nums)-1:
                res.append(forward[i-1])
                continue
            res.append(forward[i-1]*backward[i+1])
        return res
               
