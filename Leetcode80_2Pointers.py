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
            if nums[j] == nums[i-1] and nums[j]==nums[i-2]:
                # this means nums[j] is a duplicate
                j += 1
                continue
            # if nums[j] is not a duplicate
            nums[i] = nums[j]
            i += 1
            j += 1
            
        return i
                