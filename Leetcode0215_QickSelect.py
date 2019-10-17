class Solution(object):
    
    # This is a quick select implementation
    # check this video https://www.youtube.com/watch?v=MZaf_9IZCrc
    def partition(self, low, high, nums):
        '''
        
        '''
        # first chooses a pivot, here we choose high
        pivot = nums[high]
        
        # elements before(including) index i are less than pivot
        i = low - 1
        # elements between i and j are bigger than pivot
        j = low
        # elements after j needs to be processed
        # less..i|bigger|j...pivot
        
        #Second we traverse the unprocessed numbers 
        for j in range(low, high):
            # we compare nums[j] with the pivot
            if nums[j]>=pivot:
                # in this case we do not need to 
                j += 1
                continue
            # if nums[j]<pivot, we need to put it in nums[low:i+1]
            i += 1
            # Note that now nums[i]>= pivot and nums[j]<pivot, so we just need to swap them 
            nums[i], nums[j] = nums[j], nums[i]
        # At last we need to put the pivot where it is
        nums[i+1], nums[high] = nums[high], nums[i+1]
        # finnally return the index of the pivot
        return i+1
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return []
        
        low = 0
        high = len(nums)-1
        # here we need to find the k-th smallest element using quicksort
        k = len(nums)-k+1
        # we need to find a pivot that its index is k-1
        while(low < high):
            pivotIndex = self.partition(low, high, nums)
            if pivotIndex == k-1:
                return nums[pivotIndex]
            if pivotIndex > k-1:
                high = pivotIndex-1
                continue
            if pivotIndex< k-1:
                # print low, high
                low = pivotIndex+1     
        
        return nums[low]
