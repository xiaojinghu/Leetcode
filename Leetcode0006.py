class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            # print s[::2], s[1::2]
            return s[::2]+s[1::2]
        
        groupSize = 2*numRows-2
        res = [""]*numRows
        # for each letter we find its position in each group
        for i in range(len(s)):
            groupIndex = (i+1)%groupSize
            if groupIndex == 0:
                groupIndex = groupSize
            if groupIndex<=numRows:
                res[groupIndex-1] += s[i]
                continue
            groupIndex -= numRows
            res[-groupIndex-1] += s[i]
        # print res
        return "".join(res)
