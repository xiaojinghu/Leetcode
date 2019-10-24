class Solution(object):
    def getKth(self, A, B, k):
        # find the kth smallest number in A+B
        lenA = len(A)
        lenB = len(B)
        # B is always the longer one
        if len(A)>len(B):
            return self.getKth(B, A, k)
        #Case1: if there is only one valid array which must be B, the we can just return its k-th element 
        if len(A) == 0:
            return B[k-1]
        #Case2: if we just want the smallest element, then we just return the smaller one among A[0] and B[0]
        if k == 1:
            return min(A[0], B[0])
        # divide A and B both into two parts
        # A[:pa], A[pa:]
        # B[:pb], B[pb:]
        # The first two parts of A and B have k elements in total
        pa = min(k/2, len(A))
        pb = k-pa
        if A[pa-1]<=B[pb-1]:
            # the biggest element of Apart1 <= the biggest element of Bpart1, this means that the element in Apart1 cannot be the K-th smallest element, we just discard them.
            return self.getKth(A[pa:], B, pb)
        else:
             # the biggest element of Bpart1 < the biggest element of Apart1, this means that the element in Apart1 cannot be the K-th smallest element, we just discard them.
            return self.getKth(A, B[pb:], pa)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2 == 1:
            return self.getKth(nums1, nums2, (m+n+1)/2)
        else:
            ans = (self.getKth(nums1, nums2, (m+n)/2 )+self.getKth(nums1, nums2, (m+n)/2+1))/2.0
            return ans
