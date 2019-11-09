class solution(object):
    def checkWord(self, word, validLetters):
        word = word.lower()
        
        for char in word:
            if not char.isalpha():
                continue
            if char not in validLetters:
                return False
        return True

    def countValid(self, words, validLetters):
        validLetters = set(validLetters)
        count = 0
        for word in words:
            if self.checkWord(word, validLetters):
                count += 1
        return count

obj = solution()
words = ["hEllo##", "This^^"]
validLetters =  ['h', 'e', 'l', 'o', 't', 'h', 's']
print obj.countValid(words, validLetters)
