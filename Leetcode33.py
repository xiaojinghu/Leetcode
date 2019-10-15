class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        start = 0
        end = len(nums)-1
        while(start+1<end):            
            middle = (start+end)/2
            # print start, end, middle
            if nums[middle] == target:
                return middle
            if nums[start]<nums[middle]<target:
                start = middle
                continue
            if nums[start]<=target<nums[middle]:
                end = middle
                continue
            if nums[middle]<nums[start]<=target:
                end = middle
                continue
            if target<=nums[start]<nums[middle]:
                start = middle
                continue
            if nums[middle]<target<=nums[end]:
                start = middle
                continue
            if target<nums[middle]<=nums[end]:
                end = middle
                continue
            return -1
        print start, end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
            
            
            