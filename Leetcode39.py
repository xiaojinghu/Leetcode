class Solution(object):
    def dfs(self, candidates, i, target, path, result):
        # termination condition
        # print path
        if target<0:
            return
        if target == 0:
            result.append(path)
            return
        for j in range(i, len(candidates)):
            if j!=i and candidates[j] == candidates[j-1]:
                j += 1
                continue
            self.dfs(candidates, j, target-candidates[j], path+[candidates[j]], result)
                    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = [] 
        path = []
        self.dfs(candidates,  0, target, path, result)
        return result 