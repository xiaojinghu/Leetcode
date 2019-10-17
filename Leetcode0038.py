class Solution(object):   
    def count(self, s):     
        n = len(s)
        if n == 1:
            return "1" + s
       
        i = 0
        result = ""
        count = 1
        for i in range(n-1):          
            if s[i+1] == s[i]:
                # i += 1
                count += 1
            else:
                result += str(count)+s[i]
                # i += 1
                count = 1              
        result += str(count) + s[-1]           
        return result
              
            
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        return self.count(self.countAndSay(n-1))
