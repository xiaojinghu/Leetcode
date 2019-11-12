class Solution(object):
    # solution: reservoir sampling
    # here all numbers != target are ignored.
    # we just do reservoir sampling to targets
    # we treat them as a data flow. 
    # suppose a data flow a1, a2, a3, ..., and ai is the i-th element of the flow, then the probability of keeping it is 1/i
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = -1
        countTarget = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                countTarget += 1
                # i is the i-th target
                # the probability of keeping it is 1/i
                if random.randint(1, countTarget)==1:
                    index = i
        return index