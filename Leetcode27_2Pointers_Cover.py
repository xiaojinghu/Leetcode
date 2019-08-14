class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # this is a two pointer solution
        i = 0
        j = 0
        length = len(nums)
        while(i<len(nums) and j<len(nums)):
            # use non-val value to cover val value
            if nums[j]!=val:
                nums[i]=nums[j]
                i += 1
                j += 1
                continue
            length -= 1
            j += 1
                
            
        return length