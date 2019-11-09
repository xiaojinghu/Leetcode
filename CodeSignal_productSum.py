class solution(object):
    def productSum(self, num):
        digitList = map(int, list(str(num)))
        product = 1
        sum_ = 0
        for i in range(len(digitList)):
            product *= digitList[i]
            sum_ += digitList[i]
        return product - sum_

obj = solution()
print(obj.productSum(473289))