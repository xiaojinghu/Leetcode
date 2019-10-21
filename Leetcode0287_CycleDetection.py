class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        
        # step one: find the metting point
        while(slow!=fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        # find the entry of the cycle
        fast = 0
        while(slow!=fast):
            fast = nums[fast]
            slow = nums[slow]
        return fast