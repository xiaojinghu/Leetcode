class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) <=3:
            return []
        
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j!=(i+1) and nums[j]==nums[j-1]:
                    continue
                hashmap = set()
                p = j+1
                while(p<len(nums)):
                    if (target-nums[i]-nums[j]-nums[p]) in hashmap:
                        output.append([nums[i],nums[j],nums[p],target-nums[i]-nums[j]-nums[p]])
                       
                        while(p+1<len(nums) and nums[p+1]==nums[p]):
                            p += 1
                    hashmap.add(nums[p])
                    p += 1
                        
        return output
