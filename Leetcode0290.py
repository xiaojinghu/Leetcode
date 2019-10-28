class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #THIS IS ANOTHER ONE-ONE MAPPING PROBLEM
        #WE SOLVE IT USING 2 HASHMAPS
        words = str.split(' ')
        
        if len(pattern) != len(words):
            return False
        hashMap1 = {}
        hashMap2 = {}
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char not in hashMap1:
                hashMap1[char] = word
                if word in hashMap2:
                    return False
                hashMap2[word] = char
            else:
                if word not in hashMap2:
                    return False
                if hashMap1[char] != word:
                    return False
                if hashMap2[word] != char:
                    return False
        return True
        