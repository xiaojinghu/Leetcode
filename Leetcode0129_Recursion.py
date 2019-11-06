# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.totalSum = 0
    def dfs(self, root, currSum):
        if not root.left and not root.right:
            self.totalSum += currSum*10+root.val
            return
        if root.left:
            self.dfs(root.left, currSum*10+root.val)
        if root.right:
            self.dfs(root.right, currSum*10+root.val)
            
            
            
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return  0
        self.dfs(root, 0)
        return self.totalSum
