# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValid(self, root):
        if not root.left and not root.right:
            return root.val, root.val, True
        valid = True
        minRoot = root.val
        maxRoot = root.val
        if root.left:
            maxLeft, minLeft, ValidLeft = self.isValid(root.left)
            minRoot = minLeft
            if not ValidLeft or root.val<=maxLeft:
                valid  =  False
        if root.right:
            maxRight, minRight, ValidRight = self.isValid(root.right)
            maxRoot = maxRight
            if not ValidRight or root.val>=minRight:
                valid = False
        return maxRoot, minRoot, valid
                
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValid(root)[2]
        