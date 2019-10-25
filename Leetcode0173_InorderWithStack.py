# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
# THIS IS AN INORDER TRAVERSAL USING STACK
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            self.stack = []
            return 
        self.stack = [root]
        p = root
        while(self.stack and self.stack[-1].left):
            self.stack.append(self.stack[-1].left)
            
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        # The current node on top of the stack is the smallest node
        popNode = self.stack.pop()
        if popNode.right:
            self.stack.append(popNode.right)
            while(self.stack and self.stack[-1].left):
                self.stack.append(self.stack[-1].left)
        return popNode.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()