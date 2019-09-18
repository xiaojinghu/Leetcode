class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        # we can split the nums array into two parts
        # the first part: nums[start:pivot+1], nums[pivot:end+1]
        while(start+1<end):
            middle = (start+end)/2
            if nums[start]<nums[middle]:
                if nums[start]<=target<nums[middle]:
                    end = middle
                else:
                    start = middle
            else:
                if nums[middle]<target<=nums[end]:
                    start = middle
                else:
                    end = middle
    
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1