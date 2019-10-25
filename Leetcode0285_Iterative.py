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
        #The in-order successor of a node is the left-most node in its right sub-tree, if exists. 
        # if p do not has a right subtree, we know that its left tree has already been visited so the sucessor can not be in its left subtree, and since it does not has a right subtree, the successor can only be among its ancestors. Suppose this ancestor is q, then we know that p can only be in the left subtree of q, otherwise , q will be visited before p. And apparently q is the "nearest" ancestor of p, which means we need to find the root of a minimum subtree whose left subtree contains node p.
        if not p or not root:
            return None
        
        # Case1: p has right subtree, we find the leftmost node of its right subtree
        if p.right:
            sucessor = p.right
            while(sucessor.left):
                sucessor = sucessor.left
            return sucessor
        
        # Case2: p does not have right subtree, we need to find the minimum subtree where p is in its left subtree
        # sucessor means the root of the minimum left subtree
        # when we fina a smaller one, we update sucessor
        successor = None
        q = root
        while(q):
            if p.val<q.val:
                # it means p is in the left subtree of sucessor
                successor = q
                q = q.left
                continue
            if p.val == q.val:
                break
            if p.val>q.val:
                q = q.right
        return successor