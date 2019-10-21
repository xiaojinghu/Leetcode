# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        #since it is a BST, we know that all values in left tree are ledd than root.val and all values in right tree are bigger than root.val
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
        