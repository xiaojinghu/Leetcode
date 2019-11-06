# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxSum = float('-inf')
        
    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            pathSum = root.val
            self.maxSum = max([pathSum, self.maxSum])
            return pathSum
        pathSum = root.val
        leftSum = self.dfs(root.left)
        rightSum = self.dfs(root.right)
        if leftSum>0:
            pathSum += leftSum
        if rightSum>0:
            pathSum += rightSum
        self.maxSum = max([pathSum, self.maxSum])
        return max([root.val, leftSum+root.val, rightSum+root.val])
                    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        self.dfs(root)
        return self.maxSum