# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while(queue):
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                if node:
                    res.append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
                else:
                    res.append(None)
        # print res
        return res
                
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = collections.deque(data)
        # get the root
        rootVal = data.popleft()
        root = TreeNode(rootVal)
        prevLevel = collections.deque([root])
        while(prevLevel):
            size = len(prevLevel)
            for i in range(size):
                parent = prevLevel.pop()
                left = data.popleft()
                right = data.popleft()
                if left != None:
                    left = TreeNode(left)
                    prevLevel.appendleft(left)
                if right!=None:
                    right = TreeNode(right)
                    prevLevel.appendleft(right)
                parent.left = left
                parent.right = right
        return root
                