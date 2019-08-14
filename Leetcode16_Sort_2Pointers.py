class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<=2:
            return None
        
        nums.sort()
        # this variable is used to store the closest sum to target
        closestSum = float('inf') 
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                currSum = nums[i]+nums[j]+nums[k]
                if currSum == target:
                    # no pair will be more closer
                    return currSum
                if currSum>target:
                    k -= 1
                else:
                    j += 1
                # update closestSum
                if abs(currSum-target)<abs(closestSum-target):
                    closestSum = currSum
        return closestSum
            

        