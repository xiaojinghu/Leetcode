class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        # find the first occurance
        start = 0
        end = len(nums)-1
        res = [-1, -1]
        while(start+1<end):
            middle = (start+end)/2
            # print start, end, middle
            if nums[middle]==target:
                res[0] = middle
                # we check if we can find one on the left side
                # print res
                end = middle
                continue
            if nums[middle]>target:
                end = middle
                continue
            start = middle
        if nums[start] == target:
            res[0] = start
        else:
            if nums[end] == target:
                res[0] = end
            
        # find the second occurance
        start = 0
        end = len(nums)-1
        while(start+1<end):
            middle = (start+end)/2
            if nums[middle]==target:
                res[1] = middle
                # we check if we can find one on the left side
                start = middle
                continue
            if nums[middle]>target:
                end = middle
                continue
            start = middle
        if nums[end] == target:
            res[1] = end 
        else:
            if nums[start] == target:
                res[1] = start  
        return res
