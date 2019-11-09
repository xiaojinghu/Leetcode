# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    求完全二叉树的节点数目。注意完全二叉树和满二叉树Full Binary Tree的唯一区别是，完全二叉树最后一层的节点不满，而且假设最后一层有节点，都是从左边开始。 这样我们可以利用这个性质得到下面的结论：
    1.假如左子树高度等于右子树高度，则右子树为完全二叉树，左子树为满二叉树。
    2.假如高度不等，则左字数为完全二叉树，右子树为满二叉树。
    3.求高度的时候只往左子树来找。
    '''
    def getHeight(self, root):
        if not root:
            return 0
        return 1+self.getHeight(root.left)
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # we compare the height of the left subtree and the height of the right subtree
        heightLeft = self.getHeight(root.left)
        heightRight = self.getHeight(root.right)
        if heightLeft == heightRight:
            # it means that the left tree is a perfect tree, and the right tree remains a complete tree
            nodesLeft = 2**heightLeft-1
            nodesRight = self.countNodes(root.right)
        else:
            # the right tree is a prefect tree and the left tree is a complete tree
            nodesRight = 2**heightRight-1
            nodesLeft = self.countNodes(root.left)
        return nodesRight+nodesLeft+1
            