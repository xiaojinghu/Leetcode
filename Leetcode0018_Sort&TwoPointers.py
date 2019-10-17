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
        for i in range(len(nums)-3):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j!=(i+1) and nums[j]==nums[j-1]:
                    continue
                p = j+1
                q = len(nums)-1
                while(p<q):
                    if nums[i]+nums[j]+nums[p]+nums[q] == target:
                        output.append([nums[i],nums[j],nums[p],nums[q]])
                        p += 1
                        q -= 1
                        while(p<len(nums)-1 and nums[p]==nums[p-1]):
                            p += 1
                        while(q>=j+1 and nums[q]==nums[q+1]):
                            q -= 1
                        continue
                    if nums[i]+nums[j]+nums[p]+nums[q]<target:
                        p += 1
                        continue
                    if nums[i]+nums[j]+nums[p]+nums[q]>target:
                        q -= 1
                        continue
         return output
