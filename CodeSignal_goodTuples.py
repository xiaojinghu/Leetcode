class solution(object):
    def isValid(self, a, b, c):
        if a==b and a!c:
            return True

        if b==c and a!=c:
            return True

        if a==c and b!=c:
            return True

        return False

    def count(self, nums):
        count = 0
        for i in range(len(nums)-2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if self.isValid(a, b, c):
                count += 1
        return count