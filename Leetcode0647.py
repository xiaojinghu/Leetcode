class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #idea: 遍历 for (i=0; i<n; i++)，考察以i为中心的回文串个数（回文串长度为奇数）、i和i+1为中心的回文串个数（回文串长度为偶数），分别加入总的结果中。考察方法是以中心i往两边扩散。一旦发现无法实现中心对称，则可以跳过这个i。整体的时间复杂度是 o(n^2)
        count = 0
        for k in range(2*len(s)-1):
            #case1, the center is a letter in s
            if k%2==0:
                i = k/2
                j = 0
                while(i-j>=0 and i+j<len(s)):
                    if s[i-j]==s[i+j]:
                        count += 1
                        j += 1
                    else:
                        break
            else:
                i = k/2
                j = (k+1)/2
                while(i>=0 and j<len(s)):
                    if s[i] == s[j]:
                        count += 1
                        i-= 1
                        j += 1
                    else:
                        break
        return count