# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append('->'.join(path+[str(root.val)]))
            return 
        if root.left:
            self.dfs(root.left, path+[str(root.val)], res)
        if root.right:
            self.dfs(root.right, path+[str(root.val)], res)
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        return res
        