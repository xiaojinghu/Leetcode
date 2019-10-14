class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums)-1
        
        # an easy to see situation
        if nums[start]<nums[end]:
            return nums[start]
        
        # our goal is to hold the mininum inside range [start, end] while
        # keep narrowing the range util just two numbers are left in this
        # range. So we need to discard ranges that are impossibe to contaion 
        # the minimum 
        while(start+1<end):
            middle = (start+end)/2
            if nums[start]<=nums[middle]:
                start = middle
            if nums[middle]<=nums[end]:
                end = middle
        return min([nums[start], nums[end]])