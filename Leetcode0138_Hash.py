"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # build a dummy head
        dummy = Node(0, None, None)
        
        # build a hashmap to map this nodes to their copis
        nodeToCopy = {}
        
        p = head
        while(p):
            currNode = p
            newNode = Node(p.val, None, None)
            nodeToCopy[currNode] = newNode
            p = p.next
            
        p = dummy
        q = head
        while(q):
            currNode = q
            currCopy = nodeToCopy[currNode]
            if currNode.next:
                currCopy.next = nodeToCopy[currNode.next]
            if currNode.random:
                currCopy.random = nodeToCopy[currNode.random]
            #update p and q
            q = q.next
            p.next = currCopy
            p = p.next
            p.next = None
        