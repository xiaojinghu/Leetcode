class Solution(object):
    #我们考虑这样一个事实，总共有N个数字，黑名单中有n个数。那么白名单中有N-n个数字，那么我们只需要生成[0,N-n)中的一个随机数就可以了，如果这个数字在黑名单当中，我们就把它映射到一个[n,N)中一个白名单中的数字。基于上述思想，我们的算法如下:
#1. 先把所有的黑名单数字加入到哈希表中
#2. 遍历黑名单，如果黑名单的数字小于N - n，那么我们从N - 1开始往前找一个不在黑名单中的并且没有被影射过的数字，改变这个黑名单数字的映射关系。
#3. 每次随机生成一个[0,N-n)之间的数字，如果这个数字在黑名单当中，那么返回哈希表中映射的数字，否则直接返回原来的数字就可以了。

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.hashMap = {}
        self.upper = N-len(blacklist)
        # add all numbers in blacklist to the hashMap
        for num in blacklist:
            self.hashMap[num] = -1
        # map a number in the blacklist to a number in the white list
        i = N-1
        for num in blacklist:
            if num>=N-len(blacklist):
                continue
            while(i in self.hashMap):
                i -= 1
            self.hashMap[num] = i
            i -= 1
        

    def pick(self):
        """
        :rtype: int
        """
        number = random.randint(0, self.upper-1)
        if number not in self.hashMap:
            return number
        else:
            return self.hashMap[number]


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()