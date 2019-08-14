class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i is the slow runner
        # j is the fast runner
        i = 1
        j = 1
        
        while(j<len(nums)):
            if nums[j]!= nums[i-1]:
                nums[i] = nums[j]
                i += 1
                j += 1
                continue
            j += 1
        return i
                