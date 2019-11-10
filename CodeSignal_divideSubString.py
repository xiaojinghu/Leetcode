class solution(object):
    def count(num, k):
        num = str(num)
        count = 0
        for i in range(len(num)-k+1):
            currNum = num[i:i+k]

            if currNum[0] == '0':
                continue
            
            if　int(num)%int(currNum) == 0:
                count += 1
        return count
        
