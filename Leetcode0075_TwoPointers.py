class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        #idea: set 3 pointers
        
        left = 0
        mid = 0
        right = len(nums)-1
        
        while(left<= mid and mid<=right):
            if nums[mid] == 0:
                if mid == left:
                    mid += 1
                    continue
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                continue
            if nums[mid] == 1:
                mid += 1
                continue
            if nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
                continue
        