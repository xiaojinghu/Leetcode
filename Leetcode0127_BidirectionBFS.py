from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # this is a bidirectional BFS implementation
        wordDict = set(wordList+[beginWord])
        if endWord not in wordDict:
            return 0
        
        s1 = deque([(beginWord,1)])
        visited1 = {}
        s2 = deque([(endWord,1)])
        visited2 = {}
        # we start from the begin word
        l = len(beginWord)
        while(len(s1)>0 and len(s2)>0):
            if len(visited1)>len(visited2):
                # swap the two sets to search from different directions in turn
                s1, s2 = s2, s1
                visited1, visited2 = visited2, visited1
            # traverse the node in this level
            nextLevel = deque()
            while(len(s1)>0):
                currWord, currLevel = s1.pop()
                if currWord in visited1:
                    continue
                else:
                    visited1[currWord] = currLevel
                # we traverse its neighbors
                for i in range(len(currWord)):
                    for j in range(26):
                        newWord = currWord[:i]+chr(ord('a')+j)+currWord[i+1:]
                        if newWord in visited1:
                            continue
                        if newWord in visited2:
                        # this means this newWord is can both be reached by the beginWord and the endWord
                            return currLevel+visited2[newWord]
                        if newWord in wordDict:
                            nextLevel.appendleft((newWord, currLevel+1))
                # print nextLevel
            s1 = deque(nextLevel)          
                            
        return 0
