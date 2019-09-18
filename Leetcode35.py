class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        start = 0
        end = len(nums)-1
        while(start+1<end):
            middle = (start+end)/2
            if nums[middle] == target:
                return middle
            if nums[middle]<target:
                start = middle
                continue
            end = middle
        print start,end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        # check the insertion place
        return start+1