class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None

class DlinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if not node:
            return
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.next = None
        node.prev = None
        p = self.head
        node.next = p
        p.prev = node
        self.head = node
        
    def pop(self, node = None):
        if not self.head:
            return 
        if not node: node = self.tail
            # pop a node from the tail of the double linked list
        if node == self.tail:
            # check if it is also the head
            if self.head == self.tail:
                self.head = self.tail = None
                return node
            # node is the tail and not the head
            p = node.prev
            p.next = node.next
            self.tail = p
            node.prev = None
            node.next = None
            return node
        # check if p is the head
        if node == self.head:
            # node is the head not the tail
            q = self.head.next
            self.head = q
            node.prev = None
            node.next = None
            return node
        # node is not the head nor the tail     
        p = node.prev
        q = node.next
        p.next = q
        q.prev = p
        node.next = None
        node.prev = None
        return node
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyToNode = {}
        self.capacity = capacity
        self.freqToNodeList = collections.defaultdict(DlinkedList)
        self.minFreq = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode:
            return -1
        # we need to update the frequency of the corresponding node
        node = self.keyToNode[key]
        # print "node is ",node
        node.freq += 1
        self.freqToNodeList[node.freq-1].pop(node)
        self.freqToNodeList[node.freq].append(node)
        
        # Now we need to update the minimum frequency
        if self.freqToNodeList[self.minFreq].head:
            return node.val
        self.freqToNodeList.pop(self.minFreq)
        self.minFreq += 1
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key)!=-1:
            # we update the value of the corresponding node
            self.keyToNode[key].val = value
            return
        # check if we need to pop the old value out
        if self.capacity == 0:
            # check if there is an old value
            if self.freqToNodeList[self.minFreq].tail:
                popedNode = self.freqToNodeList[self.minFreq].pop()
                self.keyToNode.pop(popedNode.key)
            else:
                return 
        else:
            self.capacity -= 1
        # Now we need to insert the new key 
        newNode = Node(key, value)
        self.keyToNode[key] = newNode
        self.freqToNodeList[1].append(newNode)
        self.minFreq = 1