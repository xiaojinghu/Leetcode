"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def dfs(self, head, nodeToCopy):
        if not head:
            return None
        if head in nodeToCopy:
            return nodeToCopy[head]
        newNode = Node(head.val, None, None)
        nodeToCopy[head] = newNode
        newNode.next = self.dfs(head.next, nodeToCopy)
        newNode.random = self.dfs(head.random, nodeToCopy)
      
        return newNode
   

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeToCopy = {}
        return self.dfs(head, nodeToCopy)
