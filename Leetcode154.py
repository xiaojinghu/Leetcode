class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end  = len(nums)-1
        while(start+1<end):
            print start, end
            if nums[start]<nums[end]:
                return nums[start]
            middle = (start+end)/2
            if nums[middle]>nums[end]:
                start = middle
                continue
            if nums[middle]<nums[start]:
                end = middle
                continue
            
            if nums[middle] == nums[start]:
                start += 1
                continue
            if nums[middle] == nums[end]:
                end -= 1
                continue
        return min([nums[start], nums[end]])