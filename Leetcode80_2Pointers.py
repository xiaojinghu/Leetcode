class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #edge cases
        if not nums:
            return 0
        if len(nums) <= 2:
            return 2
                    
        # i is the slower runner to find the place to store the values
        i = 2
        # j is the faster runner to find all unique values
        j = 2

        while(j<len(nums)):
            if nums[j] == nums[i]:
                j += 1
                contiue
            if nums[i]==nums[i-1] and nums[i-1]==nums[i-2]:
                # nums[i] is a duplicate, we can need to cover it
                nums[i] = nums[j]
                i  += 1
                j += 1

        return i+1