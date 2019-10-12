class Solution(object):
    def backtrack(self, nums, i, res, path):
        if i==len(nums):
            return 
        # we add path in the result
        self.backtrack(nums, i+1, res, path)
        # we add i into the path
        res.append(path+[nums[i]])
        self.backtrack( nums, i+1, res, path+[nums[i]])
        
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        self.backtrack(nums, 0, res, [])
        return res