from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # this is a simple BFS implementation
        # note that the begin word may not be in the wordList, so we need to add it in.
        wordDict = set(wordList+[beginWord])
        if endWord not in wordDict:
            return 0
        
        queue = deque([(beginWord,1)])
        while(queue):
            currWord, currLevel = queue.pop()
            # pop the word from the dict to avoid repeated visiting
            if currWord not in wordDict:
                # it has been visited]
                continue
            wordDict.remove(currWord)
            # check the termination condition
            if currWord == endWord:
                return currLevel
            for i in range(len(currWord)):
                for j in range(ord('a'), ord('z')+1):
                    newWord = currWord[:i]+chr(j)+currWord[i+1:]
                    if newWord in wordDict:
                        # this means newWord is "connected" with currWord and hasn't been visited
                        queue.appendleft((newWord, currLevel+1))
        return 0
