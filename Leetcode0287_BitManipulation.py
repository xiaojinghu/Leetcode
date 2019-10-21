class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # THIS IS A BIT MANIPULATION IMPLEMENTATION     
        res = 0
        n = len(nums)-1
         # if there is no duplicate, we should have numbers from 1 to n, and if we count the number of ones on each bit, they should be fixed numbers.
        for i in range(32):
            mask = (1<<i)
            # count1 records how many ones appear for 1...n at bit i+1
            # count2 records how many ones appear for the whole nums array at bit i+1
            # initially they are all zeros
            count1, count2 = 0,0
            for k in range(n+1):
                if k&mask>0:
                    count1 += 1
                if (nums[k-1]&mask)>0:
                    count2 += 1
            # we know that if count1<count2, then the corresponding bit of the duplicate must be 1
            if count1<count2:
                res += mask