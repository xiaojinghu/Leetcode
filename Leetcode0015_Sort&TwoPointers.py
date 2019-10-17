class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []       
        if len(nums) <= 2:
            return []
        
        nums.sort()
        output = []
       
        for i in range(len(nums)):
            # remove duplicate i
            if i!=0 and nums[i] == nums[i-1]:
                continue
            # initialize two pointers, one traverse from i+1 and the 
            # other one traverse from the end of the list
            j = i+1
            k = len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    output.append([nums[i], nums[j], nums[k]])
                    # once we find a pair of current nums[i], nums[j], nums[k]\
                    # we skip duplicate j and k
                    j += 1
                    k -= 1
                    while(j<=len(nums)-1 and nums[j] == nums[j-1]):
                        j += 1
                    while(k>=i+1 and nums[k] == nums[k+1]):
                        k -= 1

                    continue
                if nums[i]+nums[j]+nums[k]<0:
                        j += 1
                        continue
                if nums[i]+nums[j]+nums[k]>0:
                        k -= 1
                        continue
        return output
            
