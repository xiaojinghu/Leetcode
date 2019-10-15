class Solution(object):
    def dfs(self, candidates, path, i, target, result):
        if target<0:
            return 
        if target == 0:
            result.append(path)
            return
        for j in range(i, len(candidates)):
            if j != i and candidates[j] == candidates[j-1]:
                j += 1 
                continue
            # print j, path, target
            self.dfs(candidates, path+[candidates[j]], j+1, target-candidates[j], result)
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, [], 0, target, res)
        return res