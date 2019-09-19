class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # bulls: correct position and digits
        bulls = 0
        # cows: correct digit but wrong position
        cows = 0

        # calculate bulls
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
        
        # calculate the sum of bulls and cows
        count1 = {}
        count2 = {}
        for i in range(len(guess)):
            if guess[i] not in count1:
                count1[guess[i]]=0
            count1[guess[i]] += 1
            if secret[i] not in count2:
                count2[secret[i]]=0
            count2[secret[i]] += 1
        
        total = 0
        for digit in count1:
            if digit in count2:
                total += min(count1[digit], count2[digit])
        
        cows = total - bulls
        
        return str(bulls)+'A'+str(cows)+'B'
        