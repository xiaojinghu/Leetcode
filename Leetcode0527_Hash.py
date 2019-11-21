class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """        
        abbrs = {}
        wrap = {}
        for word in words:
            if len(word)<=3:
                abbrs[word]=word
                continue
            if (word[0]+word[-1], len(word)) not in wrap:
                wrap[(word[0]+word[-1], len(word))] = []
            wrap[(word[0]+word[-1], len(word))].append(word)

        # print  wrap
        for startEndLen in wrap:
            start, end = startEndLen[0]
            length = startEndLen[1]
            if len(wrap[startEndLen]) == 1:
                word = wrap[startEndLen][0]
                abbrs[word] = start+str(length-2)+end
                continue
            # Now there may be conflicts here, we need to find the shortest prefix of each word to make it unique
            # we try from index 0
            wordList = wrap[startEndLen]
            wordSet = set(wordList)
            prefixToWord = {word[0]:wordList}
            i = 0
            while(wordSet):
                # once we find some prefix fix that will make some word unique, we add its abbreviation and pop it out from our dict
                for prefix in prefixToWord.keys():
                    if len(prefixToWord[prefix]) == 1:
                        # its prefix is prefix, the index of the last prefix is i, and the length of the middle part is length-2-i
                        word = prefixToWord[prefix][0]
                        if (length-2-i)<=1:
                            abbrs[word] = word
                        else:
                            abbrs[word] = word[:i+1]+str(length-i-2)+word[-1]
                        #pop the word out
                        prefixToWord.pop(prefix)
                        wordSet.remove(word)
                i += 1
                for word in wordSet:
                    if word[:i+1] not in prefixToWord:
                        prefixToWord[word[:i+1]] = []
                    prefixToWord[word[:i+1]].append(word)
        res = []
        for word in words:
            res.append(abbrs[word])
        return res
                