class Solution(object):
    def isPalindrome(self, word):
        for i in range(len(word)/2):
            if word[i]!=word[len(word)-1-i]:
                return False
        return True
    
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Brute force implementation will cause TLS, so will need to think of a new way to save time.
        # There are 4 conditions when word[i]+word[j] is a palindrome.
        # Case1: len(word[j])==len(word[i]), then we have word[j] == word[i].reverse(). For example: "abcd"|"dcba".
        # Case2: len(word[j])<len(word[i]), suppose word[i]="abcd", then word[j] must be "cba". We can split word[i] into two parts, the first part is a palindrome, and word[j] must be the reverse of the second part.
        # Case3: len(word[j])>len(word[i]). Suppose word[i]="abcd", then word[j] can be "edcba". We can split word[j] into two parts, the first part is a palindrome and the second part is the reverse of word[i].
        # Since for case 3, it is hard to know what that palindrome is, we can switch word[i] and word[j] and then find word[j]+word[i] is a palindrome.       
       
          # initially we put all words and its index into a lookup table
        wordToIndex = {word:index for index, word in enumerate(words)}
        res = set()
        
        for i in range(len(words)):
            currWord = words[i] 
            for k in range(len(currWord)+1):
                pf = currWord[:k]
                sf = currWord[k:]
                # case1, word[j]+word[i] is a palindrome
                if self.isPalindrome(pf):
                    # we need the reverse of the sf
                    if sf[::-1] in wordToIndex:
                        j = wordToIndex[sf[::-1]]
                        if i!=j and (j,i) not in res:
                            res.add((j, i))
                #case2, word[i]+word[j] is a palindrome
                if self.isPalindrome(sf):
                    if pf[::-1] in wordToIndex:
                        j = wordToIndex[pf[::-1]]
                        if i!=j and (i,j) not in res:
                            res.add((i,j))
        
        return map(list, list(res))
            