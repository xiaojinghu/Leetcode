class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack)):
            if i+len(needle)-1>=len(haystack):
                # print i
                return -1
            if haystack[i:i+len(needle)]== needle:
                return i
            i +=1
        return -1
