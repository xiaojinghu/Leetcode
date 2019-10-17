class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        n = len(s)
        Max = ""
        for k in range(2*n-1):
            # find the core of the palindrome
            if k%2 == 0:
                currString = s[k/2]
                j = 1
                while((k/2-j)>=0 and (k/2+j)<=len(s)-1):
                    if s[k/2-j] == s[k/2+j]:
                        currString = s[k/2-j]+currString+s[k/2+j]
                        j += 1
                    else:
                        break
                if len(currString)>len(Max):
                    Max = currString
                continue
            if k%2 == 1:
                currString = ""
                j = 0
                while((k/2-j)>=0 and((k+1)/2+j)<=len(s)-1):
                    if s[k/2-j] == s[(k+1)/2+j]:
                        currString = s[k/2-j]+currString+s[(k+1)/2+j]
                        j += 1
                    else:
                        break
                if len(currString)>len(Max):
                    Max = currString
        return Max
                
