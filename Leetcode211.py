class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.children = {}
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word: return
        currNode = self.root
        for char in word:
            if char in currNode.children:
                currNode = currNode.children[char]
                continue
            newNode = TrieNode()
            currNode.children[char] = newNode
            currNode = newNode
        currNode.isEnd = True
        
    def wordSearch(self, node, word):
        # termination condition
        if not word:
            return node.isEnd
        if word[0] in node.children:
            # print node.children, word
            return self.wordSearch(node.children[word[0]], word[1:])
        if word[0] != '.':
            return False
        for char in node.children:
            if self.wordSearch(node.children[char], word[1:]):
                return True
        return False
    
    
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.wordSearch(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("a")
# obj.addWord("ab")
# print obj.root.children["a"].children
# print obj.search("..")

