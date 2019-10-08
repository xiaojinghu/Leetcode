class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # actually we can treat the nums array as a hashtable with indice as key     
        for i in range(len(nums)):
            # for any positive number nums[i], we need to put nums[i] at index nums[i]-1
            # make sure that the index is valid
            while(1<=nums[i] and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]):
                # in this situation we need to swap the value of nums[i] and nums[nums[i]-1]
                # we must change nums[nums[i]-1] first
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # then we check
        print nums
        for i in range(len(nums)):
            # print i, nums[i]
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1