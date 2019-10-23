# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        leftInorder = inorder[:rootIndex]
        leftPreorder = preorder[1:rootIndex+1]
        rightInorder = inorder[rootIndex+1:]
        rightPreorder = preorder[rootIndex+1:]
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root
        