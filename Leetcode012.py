class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """      
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']        
        result = []        
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        
        for i in numbers:
            result.append(num/i)
            num = num-result[-1]*i
        
        string = ""
        for i in range(13):
            string += romans[i]*result[i]
            
        return string