class Solution(object):
    def binarySearch(self, nums, index1,index2, target):
        # find the leftmost and right most index of target
        # find the leftmost position
        res = [-1, -1]
        start, end = index1, index2
        while(start+1<end):
            middle = (start+end)/2
            if nums[middle] == target:
                end = middle
                continue
            if nums[middle] > target:
                end = middle
                continue
            start = middle
        # check start and end
        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end
        
        # find the rightmost position
        start, end = index1, index2
        while(start+1<end):
            middle = (start+end)/2
            if nums[middle] == target:
                start = middle
                continue
            if nums[middle] > target:
                end = middle
                continue
            start = middle
        # check start and end
        if nums[end] == target:
            res[1] = end
        elif nums[start] == target:
            res[1] = start
        return res
            
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # for this problem, we need to find number of subarrays which has k odd numbers. We can use the prefix sum strategy to calculate how many odd numbers there are in each subarray in O(n) time.
        if not nums:
            return 0
        
        counts = [0]     
        for i in range(1, len(nums)+1):
            if nums[i-1]%2==1:
                counts.append(counts[-1]+1)
            else:
                counts.append(counts[-1])
  
        # for each counts[i] we need to find counts[i]-k in counts[:i]
        res = 0
        # print counts
        for i in range(1, len(counts)):
            if counts[i]<k:
                continue
            start, end = self.binarySearch(counts, 0, i-1, counts[i]-k)
            if start == -1:
                continue
            # print i, start, end
            res += end-start+1
        return res