class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        # nums[:i] contains no duplicate
        # nums[i:] are not processed
        while(j<len(nums)):
            # nums[i:j] contains duplicates
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1