# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def dfsSerialize(self, root, res):
        # First order taversal
        if not root:
            res.append(None)
            return
        res.append(root.val)
        self.dfsSerialize(root.left, res)
        self.dfsSerialize(root.right, res)   
        return
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.dfsSerialize(root, res)
        # print res
        return res
        
    def dfsDeserialize(self, data):
        root = data.popleft()
        if root == None:
            return root
        root = TreeNode(root)
        # we should obtain its left tree and right tree
        left = self.dfsDeserialize(data)
        right = self.dfsDeserialize(data)
        root.left = left
        root.right = right
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data)
        return self.dfsDeserialize(data)