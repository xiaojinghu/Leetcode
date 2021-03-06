from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # first check if the end word in  the wordList
        if endWord not in wordList:
            return 0
        
        # the preprocessing part: build the all_combo_dict
        # we should build a graph, if two words can be tranformed from each other, we can connect these two words.
        # here we can have a trick, we can connect these two words through an intermediate word which is generated by repalce one letter in a word by a special charactor "*"
        wordList.append(beginWord)
        # all_combo_dict map the intermediate word to a list of original word
        all_combo_dict = {}
        # transformations maps the original word to a list of intermediate word
        transformations = {}
       
        for word in wordList:
            transformations[word] = []
            # for each letter in a word, replace one letter in the word by '*'
            # add the newly created word as key in the dict
            # add the original word in the wordList with key as generic state
            for i in range(len(word)):
                # generated an intermediate word of this word
                newWord = word[:i]+'*'+word[i+1:]
                if newWord not in all_combo_dict:
                    all_combo_dict[newWord] = []
                # add a path from the intermediate word to the original word
                all_combo_dict[newWord].append(word)
                # add a path from the original word to the intermediate word
                transformations[word].append(newWord)
                
        # keep a visited set to avoid cycle
        # here we use a BFS to traverse the graph
        visited = set()
        queue = deque([(beginWord, 1)])
        while(queue):
            currWord, level = queue.pop()
            if currWord == endWord:
                return level
                break
            if currWord in visited:
                continue
            visited.add(currWord)
            # find all the generic transformations of the current word
            gTrans = transformations[currWord]
            # for each transformation of the current word, find if it is also an transformation of other words
            # add all word that share a transformed word with the current word, i.e., they are connected
            for trans in gTrans:
                for word in all_combo_dict[trans]:
                    # here word is connected with current word
                    if word not in visited:
                        queue.appendleft((word, level+1))
        return 0
