class solution(object):
    def check(self, account):
        # first check the length
        if len(account)!=8:
            return False
        # then check if each dight is an hexadecimal
        for char in account:
            if char not in '0123456789ABCDEF':
                return False

        checkSum = int('0x'+account[:2], 16)
        digits = int('0x'+account[2:], 16)
        digits = str(digits)
        realCheckSum = 0
        for char in digits:
            realCheckSum += int(char)
        return realCheckSum==checkSum

    def isValid(self, accountNums):
        res = []
        for item in accountNums:
            if self.check(item):
                res.append("Valid")
            else:
                res.append("Invalid")
        return res

obj = solution()
print obj.isValid(["BADF00D5"])