class Solution(object):
    def backtracking(self, nums, i, path, res):
        res.append(path)
        # for each number in nums[i:], we choose one to add into our path
        # we need to avoid duplicate in this situation
        for j in range(i, len(nums)):
            if  j == i or nums[j]!=nums[j-1]:
                #this means nums[j] is the first unique one behind i
                self.backtracking(nums,j+1,path+[nums[j]], res )
        return 
        
            
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        path = []
        self.backtracking(nums, 0, path, res)
        return res
        
        
