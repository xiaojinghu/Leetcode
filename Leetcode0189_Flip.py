class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # this is a flip implementation
        # first we flip the first n-k elements
        # then we flip the last k elements 
        # the we flip the whole list
        n =len(nums)
        k = k%n
        for i in range((n-k)/2):
            nums[i], nums[n-k-i-1] = nums[n-k-i-1], nums[i]
            
        # print nums
        for i in range(n-k, (2*n-k+1)/2):
            nums[i],nums[2*n-k-i-1] = nums[2*n-k-i-1], nums[i]
        # print nums
        for i in range(n/2):
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
