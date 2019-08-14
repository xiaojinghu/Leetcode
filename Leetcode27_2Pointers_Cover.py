class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # this is a two pointer solution
        # i is the slo runner
        # j is the fast runner that points to values!=val
        i = 0
        j = 0
        while(j<len(nums)):
            if nums[j]!=val:
                nums[i] = nums[j]
                i += 1
                j += 1
                continue
            j += 1
        # note that after we copied nums[j] to nums[i], we actually increament 
        # i by one, so here we return i
        return i