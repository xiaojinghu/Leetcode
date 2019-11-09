class Solution(object):
    def missingRange(self, lower, upper):
        '''
        return the  missing range bettween lower and upper
        rtype: list of int
        '''
        if lower==upper or lower == upper-1:
            return []
        if upper-2 == lower:
            return [upper-1]
        return [lower+1, upper-1]
    
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            return [str(lower)+'->'+str(upper)]
        res = []
        lower -= 1
        upper += 1
        nums.append(upper)
        for i in range(len(nums)):
            # the current missing range should be lower and nums[i]
            currRange = self.missingRange(lower, nums[i])
            if currRange:
                res.append(currRange)
            lower = nums[i]
        print res
        for i in range(len(res)):
            res[i] = map(str, res[i])
        return ['->'.join(x) for x in res]