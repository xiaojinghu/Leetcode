class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        currWord = ""
        banned = set(banned)
        count = {}
        for char in paragraph.lower():
            if char.isalpha():
                currWord += char
            else:
                if not currWord:
                    continue
                if currWord in banned:
                    currWord = ""
                else:
                    if currWord not in count:
                        count[currWord] = 0
                    count[currWord] += 1
                    currWord = ""
        if currWord and currWord not in banned:
            if currWord not in count:
                count[currWord] = 0
            count[currWord] += 1
        maxWord = ""
        maxCount = 0
        print count
        for key in count:
            val = count[key]
            if val>maxCount:
                maxWord = key
                maxCount = val
        return maxWord