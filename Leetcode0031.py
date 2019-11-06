class Solution(object):
    def nextPermutation(self, s):
        """
        :type s: List[int]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # idea: 
        # 7 2 5 (2) 3 1
        # 7 2 5 3 (1) 2
        # 7 (2) 5 3 2 1
        # 7 3 1 2 (2) 5
        # 其中()中的数字表示next permutation改变原数字的最高位。比如对于725321来说，由于5321由于从最低位到最高位是升序排列，已经达到该四位数字permutation的最大值。这时不得不改变第5位的2来增加数值。如何改变？为了使增量最小，在（5，3，2，1）中找一个最小的比2大的数，即数字3。用3替换2，而剩下5, 2, 2, 1四个数字要组成最低4位。由于第2位已经从2增加到3，同样为了使增量最小，我们希望剩下的最后4位数尽可能小。
        #1. 从低位向高位（从右向左）找第一个递减的数：s[i]<s[i+1]。如果不存在，则表明该permutation已经最大，next permutation为当前序列的逆序。
        #2. 在s[i+1:]中找一个最小的s[j]，使得s[j]>s[i], 也就是说s[j]>s[i]>=s[j+1], 交换s[i], s[j]。
        #3. 对s[i+1:]进行排序。 由于s[i]>=s[j+1]，所以s[i+1:]实际上为降序排列，我们只需将 s[i+1:]逆序。
        
        if not s:
            return []
        if len(s) == 1:
            return s
        i = len(s)-2
        #Starting from the right side of s, find the first s[i] that satisfies s[i]<s[i+1]
        # if we cannot find such s[i], then it means that the current permutation is the greatest one.
        while(i>=0):
            if s[i]<s[i+1]:
                break
            i -= 1
        if i == -1:
            # we did not find such s[i], return the reverse of s
            for i in range(len(s)/2):
                tmp = s[i]
                s[i] = s[len(s)-i-1]
                s[len(s)-i-1] = tmp
            return
        # else, we find an s[i]<s[i+1]
        # now we need to find an smallest s[j] from s[i+1:] satisfying s[j]>s[i]. Since s[i+1:] is desending, we can start from the right, the first s[j]>s[i] is the smallest one.
        j = len(s)-1
        while(j>=i+1):
            if s[j]>s[i]:
                break
            j -= 1
        # swap s[i], s[j]
        s[i], s[j] = s[j], s[i]
        
        # reverse s[i+1:]
        for j in range((len(s)-i-1)/2):
            s[i+1+j] ,s[len(s)-1-j] =  s[len(s)-1-j], s[i+1+j]
        return