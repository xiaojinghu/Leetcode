class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if  len(nums)==1:
            return 0
        
        # try both end points to see if they are peaks
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        # we have at least 3 numbers in nums and neither of  the end points is peak 
        start = 1
        end = len(nums)-2
        while(start+1<end):
            middle = (start+end)/2
            print start, end, middle
            if nums[middle]>nums[middle-1] and nums[middle]>nums[middle+1]:
                return middle
            if nums[middle]>=nums[start] and nums[middle]>=nums[end]:
                start += 1
                end -= 1
                continue
            if nums[middle]<nums[start]:
                end = middle
                continue
            if nums[middle]<nums[end]:
                start = middle
                continue
            
        if nums[start]>nums[start-1] and nums[start]>nums[start+1]:
            return start
        if nums[end]>nums[end-1] and nums[end]>nums[end+1]:
            return end