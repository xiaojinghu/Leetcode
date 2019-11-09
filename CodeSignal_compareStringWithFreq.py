class solution(object):
    def swappable(self, a, b):
        if len(a) != len(b):
            return False

        countA = {}
        countB = {}
        for i in range(len(a)):
            charA = a[i]
            charB = b[i]
            if charA not in countA:
                countA[charA] = 0
            if charB not in countB:
                countB[charB] = 0
            countA[charA] += 1
            countB[charB] += 1

        #check if a and b have the same set of letters
        letterA = set(countA.keys())
        letterB = set(countB.keys())

        for letter in letterA:
            if letter not in letterB:
                return False
        if len(letterA) != len(letterB):
            return False

        # check if countA and countB have same ferqs
        countFreqA = {}
        countFreqB = {}

        for letter in countA.keys():
            freqA = countA[letter]
            freqB = countB[letter]
            if freqA not in countFreqA:
                countFreqA[freqA] = 0
            if freqB not in countFreqB:
                countFreqB[freqB] = 0
            countFreqA[freqA] += 1
            countFreqB[freqB] += 1

        for freq in countFreqA.keys():
            if freq not in countFreqB or countFreqB[freq] != countFreqA[freq]:
                return False

        return len(set(countFreqA.keys())) == len(set(countFreqB.keys()))