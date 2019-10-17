class solution(object):

    def dfs(self, word1, word2, i, j, path):
        # termination condition
        if i>=len(word1) or j>=len(word2):
            if len(path) == len(word2) and path[-1]-path[0]+1 != len(path):
                # we've found an valid solution
                return True
            return False

        # this means we need to find word2[j] in word1[i:]
        for k in range(i, len(word1)):
            if word1[k] == word2[j]:
                # we find the next letter
                if self.dfs(word1, word2, k+1, j+1, path+[k]):
                    return True
        return False


    def isKangaroo(self, word1, word2):
        """
        determin if word2 is the kangaroo word of word1.
        XXXaXbXc, abc should return True.
        XXXabcXXX should return false because all letters should not 
        be connected together.
        """
        if len(word1)<=len(word2):
            return False 

        return self.dfs(word1, word2, 0, 0, [])



solutionIns = solution()
print solutionIns.isKangaroo('abcd', 'abc')
print solutionIns.isKangaroo('abccd', 'abc')
# print solutioonIns.isKangaroo('abcd', 'abc')

        



