class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        i = 0
        j = 0
        
        while(j<len(nums)):
            if nums[i] != 0:
                i += 1
                j += 1
                continue
            if nums[j] == 0:
                j += 1
                continue
            # no i points to the first 0, j points to the first non zero after i, we need to swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # now i points to a non-zero and j points to a zero, and there will be all zeros between them
            i += 1