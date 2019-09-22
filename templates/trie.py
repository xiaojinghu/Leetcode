class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.children = {}
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if not word:
            return 
        currNode = self.root
        for char in word:
            if char in currNode.children:
                currNode = currNode.children[char]
                continue
            newNode = TrieNode()
            # add this newNode as child of the current node
            currNode.children[char] = newNode
            currNode = newNode
        currNode.isEnd = True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.isEnd
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True