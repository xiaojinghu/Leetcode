class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """   
        
        #idea: 设置一个Map和一个Set。Map是从缩写到原单词(数组)的映射。Set盛装所有仍需要进一步求缩写的原单词，初始化的时候则装所有的原单词。
        #在每次循环中，把Set里所有的单词都求其缩写加入Map，清空Set。然后查看Map的所有元素，对于那些仍然对应多个原单词的缩写，就把这些原单词加入Set。清空Map。
        #重复这样的循环直至Set不再有元素。
        
        abbrToWord = {}
        wordToAbbr = {} 
        # we try from index 0
        wordSet = set(words)
        # Initiazation of abbrs
        i = 0
        for word in wordSet:
            if len(word)<=3:
                abbr = word
            else:
                abbr = word[0]+str(len(word)-2)+word[-1]
            if abbr not in abbrToWord:
                abbrToWord[abbr] = []
            abbrToWord[abbr].append(word)
                
        while(wordSet):
            # once we find some abbr that will make some word unique, we add its abbreviation and pop it out from our dict
            for abbr in abbrToWord:
                if len(abbrToWord[abbr]) == 1:
                    word = abbrToWord[abbr][0]
                    wordToAbbr[word] = abbr
                    wordSet.remove(word)
            i += 1
            # Reinitialize abbrToWord
            abbrToWord = {}
            for word in wordSet:
                if len(word)-i-2<=1:
                    abbr = word
                else:
                    abbr = word[:i+1]+str(len(word)-i-2)+word[-1]
                if abbr not in abbrToWord:
                    abbrToWord[abbr] = []
                abbrToWord[abbr].append(word)
                               
        res = []
        for word in words:
            res.append(wordToAbbr[word])
        return res
                