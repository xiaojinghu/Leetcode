class Solution(object):
    def getKth(self, A, B, k):
        # find the kth smallest number in A+B
        lenA = len(A)
        lenB = len(B)
        # B is always the longer one
        if len(A)>len(B):
            return self.getKth(B, A, k)
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        # divide A and B both into two parts
        # A[:pa], A[pa:]
        pa = min(k/2, len(A))
        # B[:pb], B[pb:]
        pb = k-pa
        if A[pa-1]<=B[pb-1]:
            return self.getKth(A[pa:], B, pb)
        else:
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