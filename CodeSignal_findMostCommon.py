class solution(object);
def findMostCommon(self, nums):
    mostCommonNum = []
    countMostCommon = 0
    count = {}

    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] >countMostCommon:
            mostCommonNum = [num]
            countMostCommon = count[num]
            continue
        if count[num] == countMostCommon:
            mostCommonNum.append(num)
            
    return mostCommonNum