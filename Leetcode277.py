# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        i = 0
        # have a initial guess that the celebrity is 0
        guess = 0
        while(i<n):
            if i == guess:
                i += 1
                continue
            if not knows(i, guess):
                # this means that we need to update guess to i
                guess = i
            i += 1
        
        # check if guess is the celebrity
        for i in range(n):
            if i == guess:
                continue
            if knows(i, guess) and not knows(guess, i):
                continue
            return -1
        return guess
        