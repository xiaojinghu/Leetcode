# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # The inorder traversal of an BST is a sorted array
    def inorderTraversal(self, root, res):
        if not root:
            return 
        if root.left:
            self.inorderTraversal(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right, res)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.inorderTraversal(root, res)
        if not res or len(res)==1:
            return True
        for i in range(1, len(res)):
            if res[i]<=res[i-1]:
                return False
        return True