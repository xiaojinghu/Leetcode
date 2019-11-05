class Solution(object):
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
        if not b:
            return a
        return self.gcd(b, a%b)
    
    
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums)==1:
            return nums[0] == 1
        gcd = self.gcd(nums[0], nums[1])
        for i in range(2, len(nums)):
            gcd = self.gcd(gcd, nums[i])
        return gcd == 1
        