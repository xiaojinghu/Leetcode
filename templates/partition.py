def partition(self, low, high, nums):
    '''
     This function aims to partition  nums[low:high+1] according to a pivot so 
     that the left part of nums is less than pivot and the right part of nums
     is bigger than or equal to pivot.
     check thi video check this video: https://www.youtube.com/watch?v=MZaf_9IZCrc   
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
            # in this case we do nothing
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