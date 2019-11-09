class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # idea:
        # we know that the length of the result list must be k, are the result list must be a subarray of arr, so we just need to find the starting index of the result list.
        # Initialization. start must be in [0, len(arr)-k]
        left = 0
        right = len(arr)-k
        while(left+1<right):
            middle = (left+right)/2
            # now the candidate result list is nums[middle:middle+k]
            # we need to decide which way we go, to the left or to the right
            # we compare whether arr[middle] is closer to x or arr[middle+k] is closer to x
            if abs(x-arr[middle]) <= abs(x-arr[middle+k]):
                # it means arr[middle+1:middle+1+k] is closer to x, we need to move to the right
                right = middle
                continue
            left  = middle
        print left, right
        # check start and end
        if left+k>=len(arr) or abs(x-arr[left]) <= abs(x-arr[left+k]):
            return arr[left:left+k]
        return arr[right:right+k]