# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        # BFS implementation
        queue = collections.deque()
        
        if root:
            queue.appendleft(root)
        
        res = []
        while(queue):
            size = len(queue)
            currLevelSum = 0
            for i in range(size):
                currNode = queue.pop()
                currLevelSum += currNode.val
                if currNode.left:
                    queue.appendleft(currNode.left)
                if currNode.right:
                    queue.appendleft(currNode.right)
            res.append(float(currLevelSum)/ size)
        return res