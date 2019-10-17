class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #In this case s cannot be empty
        convert_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"IX":9, "IV":4, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        res = 0
        i = 0
        while(i<len(s)):
            if i+1<len(s):
                if s[i]+s[i+1] in convert_dict:
                    res += convert_dict[s[i]+s[i+1]]
                    i += 2
                    continue
            res += convert_dict[s[i]]
            i += 1
        return res
