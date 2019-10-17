class Solution(object):  
    def backtrack(self,  path, digits, i, letters, results):
        if len(path) == len(digits):
            results.append(path)
            return
        for letter in letters[digits[i]]:
            self.backtrack(path+letter, digits, i+1, letters, results)
        
       
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
    
        letters = {"2":['a','b','c'],
                "3":['d','e','f'],
                "4":['g','h','i'],
                "5":['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        results = []
        self.backtrack("", digits, 0, letters, results)
        return results
        