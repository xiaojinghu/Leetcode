# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while(stack):
             # push all the leftmost nodes in the stack till there are no leftmost nodes
            while(stack[-1].left):
                stack.append(stack[-1].left)
            
            while(stack):
                currNode = stack.pop()
                res.append(currNode.val)
                if not currNode.right:
                    continue
                else:
                    stack.append(currNode.right)
                    break
        return res
                                
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # Common approach: inorder travesal and sorting
        oriInorder = self.inorder(root)
        sortedInorder = sorted(oriInorder)
        oriToSorted = {}
        for i in range(len(oriInorder)):
            oriVal = oriInorder[i]
            sortedVal = sortedInorder[i]
            oriToSorted[oriVal] = sortedVal

        # BFS the tree to swap the values
        queue = collections.deque([root])
        while(queue):
            currNode = queue.pop()
            currNode.val = oriToSorted[currNode.val]
            if currNode.left:
                queue.appendleft(currNode.left)
            if currNode.right:
                queue.appendleft(currNode.right)