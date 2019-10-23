# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd, indexMap):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # print inStart, inEnd, postStart, postEnd
        if inStart>inEnd or postStart>postEnd:
            return None
        root = TreeNode(postorder[postEnd])
        rootIndex = indexMap[root.val]
        leftInStart = inStart
        leftInEnd = rootIndex-1
        leftPostStart = postStart
        leftPostEnd = rootIndex-inStart+postStart-1
        root.left = self.build(inorder, leftInStart, leftInEnd, postorder, leftPostStart, leftPostEnd, indexMap)
        rightInStart = rootIndex+1
        rightInEnd = inEnd
        rightPostStart = leftPostEnd+1
        rightPostEnd = postEnd-1
        root.right = self.build(inorder, rightInStart, rightInEnd, postorder, rightPostStart, rightPostEnd, indexMap)
        return root
        
    def buildTree(self, inorder, postorder):
        indexMap = {}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(inorder)-1, indexMap)
        