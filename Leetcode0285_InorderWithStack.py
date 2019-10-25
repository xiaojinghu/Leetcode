# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        stack = [root]
        
        # inorder traversal of the tree
        # we need to pop twice
        FLAG = False
        while(stack):
            while(stack and stack[-1].left):
                stack.append(stack[-1].left)
            
                
            while(stack):
                currNode = stack.pop()
                if FLAG:
                    return currNode
                if currNode.val == p.val:
                    FLAG = True
                if currNode.right:
                    stack.append(currNode.right)
                    break
        return None
        