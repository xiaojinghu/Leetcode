class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):
    # Implementation: linked hash map
    # use hash map to implement O(1) look up
    # use double-linked list to maintain the order and implement O(1) insertion and deletion
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            if  self.tail == node:
                return node.val
            # rearrange this element to the tail of the list
            # delete it from the list
            if self.head == node:
                q = node.next
                self.head = q
                q.prev = None
                node.next = None
                node.prev = None
            else:
                p = node.prev
                q = node.next
                p.next = q
                q.prev = p
                node.next = None
                node.prev = None
            # insert it in the end of the list
            p = self.tail
            p.next = node
            node.prev = p
            self.tail = node
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #Case1, the key is already present
        if self.get(key) != -1:
            self.map[key].val = value
            return
        
        #Case2, the key is not in the cache
        # build a new Node
        newNode = Node(key, value)
        # add this node to the map
        self.map[key] = newNode
        # append this node to the end of the list
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            
        # we decide if we need to pop the least recent node
        if self.capacity>0:
            # no need to pop
            self.capacity -= 1
            return 
        # pop the least recent node from the double linked list
        # and remove the key from the map
        self.map.pop(self.head.key)
        p = self.head.next
        p.prev = None
        self.head = p
            
       
       
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)