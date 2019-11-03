# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum, path, res):
        if not root:
            return 
        if not root.left and not root.right and root.val == sum:
            res.append(path+[root.val])
        if root.left:
            self.dfs(root.left, sum-root.val, path+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, path+[root.val],res)
            
            
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.dfs(root, sum, path, res)
        return res