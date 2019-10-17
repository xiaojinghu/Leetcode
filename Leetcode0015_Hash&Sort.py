class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=2:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip duplicate i except the first one
            if i!=0 and nums[i]==nums[i-1]:
                continue
            # now we need to solve a two sum problem where
            # nums = nums[i+1:] and terget == -nums[i] and all solutions
            # must be unique
            hashmap = set()
            j = i+1
            while(j<len(nums)):
                if (-nums[i]-nums[j]) in hashmap:
                    res.append([nums[i], nums[j],-nums[i]-nums[j]])
                    # once we find a pair for nums[i],nums[j], we do not need to find the pair for the same j
                    while(j+1<len(nums) and nums[j+1]==nums[j]):
                        j += 1
                hashmap.add(nums[j])
                j += 1
                
        return res
