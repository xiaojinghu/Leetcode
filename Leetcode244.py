class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordToIndice = {}
        for i in range(len(words)):
            word = words[i]
            if word not in self.wordToIndice:
                self.wordToIndice[word] = []
            self.wordToIndice[word].append(i)
        
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indice1 = self.wordToIndice[word1]
        indice2 = self.wordToIndice[word2]
        minDis = float('inf')
        for i in range(len(indice1)):
            for j in range(len(indice2)):
                minDis = min(abs(indice1[i]-indice2[j]), minDis)
        return minDis
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)