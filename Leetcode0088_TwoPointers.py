class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # idea: we need to insert nums2 into nums1, if we start at the front, then we will be needing to move elments in nums1 forward to spare space. To avoid this situation, we can start at the end of nums1
        i = m-1
        j = n-1
        k = m+n-1
        while(k>=0):
            # print i, j, k, nums1
            if i>=0 and j>=0:
                if nums1[i]>=nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
                continue
            if i>=0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                continue
            if j>=0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1