class Solution(object):  
    def cartesianProduct(self,  digits, dict_):
        if not digits:
            return []
        if len(digits) == 1:
            return dict_[digits[0]]       
        result = []
        for string in self.cartesianProduct(digits[:-1], dict_):
                for letter in dict_[digits[-1]]:
                    result.append(string + letter)
        return result
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
    
        dict_ = {"2":['a','b','c'],
                "3":['d','e','f'],
                "4":['g','h','i'],
                "5":['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        
        return self.cartesianProduct(digits, dict_)
