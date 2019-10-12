class Solution(object):
    def backtracking(self, nums, i, path, res):
        # temination condition
        if i>= len(nums):
            return 
        # Suppose path is an existing solution and now we are at
        # we have two choises at position i, add nums[i] to path or not
        
        # case 1: do not add nums[i], build other candidates
        self.backtracking(nums, i+1, path, res)
        # case 2: add nums[i]
        res.append(path + [nums[i]])
        # build other candidates
        self.backtracking(nums, i+1, path+[nums[i]], res)
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        self.backtracking(nums, 0, [], res)
        return res