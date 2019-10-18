class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        nums.sort()
        for i in range(len(nums)-2):
            # find the first unique elem
            if i == 0 or nums[i]!=nums[i-1]:
                j = i+1
                k = len(nums)-1
                while(j<k):
                    if j!=i+1 and nums[j]==nums[j-1]:
                        j += 1
                        continue
                    if k!=len(nums)-1 and nums[k]==nums[k+1]:
                        k -= 1
                        continue
                    if nums[j]+nums[k] == -nums[i]:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        continue
                    if nums[j]+nums[k] < -nums[i]:
                        j += 1
                        continue
                    if nums[j]+nums[k] > -nums[i]:
                        k -= 1
                        continue
        return res