class solution(object):
    def coolFeature(self, a, b, queries):
        countA = {}
        countB = {}
        # initialize the count map
        for num in a:
            if num not in countA:
                countA[num] = 0
            countA[num] += 1

        for num in b:
            if num not in countB:
                countB[num] = 0
            countB[num] +=1

        res = []

        for i in range(len(queries)):
            query = queries[i]
            if len(query) == 3:
                index = query[1]
                newNum = query[2]
                prevNum  = b[index]
                # modify b and countB
                countB[prevNum] -= 1
                if countB[prevNum] == 0:
                    countB.pop(prevNum)
                if newNum not in countB:
                    countB[newNum] = 1
                else:
                    countB[newNum] += 1
                continue
            target = query[1]
            count = 0
            for num in countA.keys():
                if target-num not in countB:
                    continue
                count += countA[num] * countB[target-num]
            res.append(count)
        return res
