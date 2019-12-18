# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isEqual(self, s, t):
        if not s:
            return not t
        if not t:
            return not s
        return s.val==t.val and self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)
       
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return not t
        if not t:
            return True
        if self.isEqual(s, t):
            return True
        return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)
        