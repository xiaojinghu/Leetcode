class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # narrow the range of the duplicate by binary search
        # note that here buttom and top donot mean indice, they mean the 
        # range [buttom, top], this is the range where the duplicate lies
        buttom = 1
        top = len(nums)
        
        while(buttom+1<top):
            # we find the medium of the range, [buttom, top]
            medium = (buttom+top)/2
            # we count how many numbers in nums <= medium
            count = 0
            for num in nums:
                if num <= medium:
                    count += 1
            if count>medium:
                # the duplicate will be in range [1, medium]
                top = medium
            else:
                buttom = medium+1
        count = 0       
        for num in nums:
            if num<=buttom:
                count += 1
        if count<=buttom:
            return top
        return  buttom
                