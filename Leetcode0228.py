class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        res = []
        for i in range(len(nums)):
            if not res:
                res.append([nums[i]])
                continue
            else:
                #check if we can add this number to the last range
                lastRange = res[-1]
                if len(lastRange) == 1:
                    if nums[i] == lastRange[0]+1:
                        lastRange.append(nums[i])
                        continue
                    # we need to assign an new range
                    res.append([nums[i]])
                    continue
                if nums[i] == lastRange[1]+1:
                    lastRange[1] += 1
                    continue
                # we need a new range
                res.append([nums[i]])
        for i in range(len(res)):
            item = res[i]
            item = map(str, item)
            res[i] = item
        return ['->'.join(x) for x in res]
        
            