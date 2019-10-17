class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # actually we can treat the nums array as a hashtable with indice as key     
        for i in range(len(nums)):
            # for any positive number nums[i], we need to put nums[i] at index nums[nums[i]-1]
            # Note this is a while loop, after each swap we are sending nums[i] to its correct position
            # but when we swap we get a new value and it may still not be in the correct position, that's
            # why we need a while loop. 
            while(nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1] != nums[i]):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            # after the while loop we are making sure that nums[i]<0(which will either be 
            # either occupied later or stay vacant) or nums[i] = i+1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
