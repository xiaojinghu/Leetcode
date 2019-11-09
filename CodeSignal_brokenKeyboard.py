class solution(object):
    def isValid(self, word, validLetters):
        for char in word:
            if char.isalpha():
                if char not in validLetters:
                    return False
            else:
                continue
        return True


    def countValid(self, words, validLetters):
        validLetters = set(validLetters)
        words = words.strip()
        words = words.split(' ')
        
        count = 0
        for word in words:
            word = word.lower()
            if self.isValid(word, validLetters):
                count += 1
        return count

obj = solution()
a = "Hello, my dear friend!"
b = ['h', 'e', 'l', 'o', 'm']
print obj.countValid(a, b)
