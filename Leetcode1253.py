class Solution(object):
   
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        if upper+lower>sum(colsum):
            return []
        rowpick = set()
        row1= [0]*len(colsum)
        row2 = [0]*len(colsum)
        for i in range(len(colsum)):
            if colsum[i] == 2:
                row1[i] = 1
                row2[i] = 1
            if colsum[i] == 1:
                # pickone from row1 and row2 to be one
                rowpick.add(i)
                
        count1 = upper-sum(row1)
        count2 = lower-sum(row2)
        if count1<0 or count2<0:
            return []
        if count1+count2!=len(rowpick):
            return []
        count = 0
        for i in rowpick:
            if count<count1:
                row1[i] = 1  
                count += 1
                continue
            row2[i] = 1
        return [row1, row2]
            