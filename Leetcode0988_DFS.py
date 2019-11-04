# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.minString = ''
    def dfs(self, root, currString):
        if not root:
            return
        if not root.left and not root.right:
            if not self.minString:
                self.minString = chr(root.val+ord('a'))+currString
            else:
                strings = [chr(root.val+ord('a'))+currString, self.minString]
                strings.sort()
                self.minString = strings[0]
            return
        if root.left:
            self.dfs(root.left, chr(root.val+ord('a'))+currString)
        if root.right:
            self.dfs(root.right, chr(root.val+ord('a'))+currString)
        
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.dfs(root, "")
        return self.minString
        