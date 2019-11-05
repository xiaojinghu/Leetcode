class Solution(object):
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
  
        # now we need to find two indice i,j where nums[i:j+1] contains k odd numbers, which is equal to find two indice i, j such that counts[j]-counts[i](j>i) = k. If we use brutal force, then it will take O(n^2) time. We can use hashmap to achieve an O(n) solution
        hashMap = {}
        for i in range(len(counts)):
            if counts[i] not in hashMap:
                hashMap[counts[i]] = 0
            hashMap[counts[i]] += 1
        
        res = 0
        for count in hashMap.keys():
            if count-k in hashMap:
                res += hashMap[count-k]*hashMap[count]
        return res
      