class Solution(object):   
    def subMatch(self, s, p, i, j, memo):
        """
        this mathod matches s[i:] to p[j:], p cannot start with *
        """
        # termination condition 1: already calculated
        if (i, j) in memo:
            return memo[(i,j)]
        # termination condition 2: p[j:] is empty. In this situation, s[i:] must be empty
        if j == len(p):
            memo[(i,j)] = (i==len(s))
            return memo[(i,j)]
        # termination condition 3: p[j:] has only one char
        if j == len(p)-1:
            memo[(i,j)] = i == len(s)-1 and p[j] in [s[i], '.']
            return memo[(i,j)]
        if j <= len(p)-2:
            # remember that there could be a '.*' combination so first check the second char
            if p[j+1] == '*':
                if i>=len(s):
                    # the only possibility of matching is just skip p[j]+p[j+1]
                    memo[(i,j)] = self.subMatch(s, p, i, j+2, memo)
                    return memo[(i,j)]
                # we could match zero of one or mulitiple p[j]
                # first try zero
                if self.subMatch(s, p, i, j+2, memo):
                    memo[(i,j)] = True
                    return memo[(i,j)]
                # try one or multiple match
                if p[j] in ['.', s[i]] and self.subMatch(s,p, i+1, j, memo):
                    memo[(i,j)] = True
                    return memo[(i,j)]
            else:
                if i>=len(s):
                    memo[(i,j)] = False
                    return memo[(i,j)]
                memo[(i,j)] = p[j] in ['.', s[i]] and self.subMatch(s,p,i+1, j+1, memo)
                return memo[(i,j)]
                
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #THIS IS A RECURSION IMPLEMENTATION
        memo = {}
        return self.subMatch(s, p, 0, 0, memo)
        