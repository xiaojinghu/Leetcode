class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

#The basic idea of Morris Traversal is that: 
#    For current Node Cur, we use the right most leaf of its left 
#    child to record the location of Cur.

#Steps of Morris inorder traversal
# 1. if currNode.left is None: 
#         visit currNode and set currNode = currNode.right;
# 2. if currNode.left is not None:
#         find the predesessor in the left subtree of currNode(the rightmost
#         node of the left subtree of currNode);
#         a). if predesessor.right is None, then:
#                 predesessor.right = currNode
#                 currNode = currNode.left
#         b). if predesessor.right == currNode:
#                 predesessor.right = None （restore the structure of the tree)
#                 visit currNode
#                 currNode = currNode.right
# 3. repeat step1 and step2 till currNode == None

def morrisInorder(root):

    #Initailization of currNode and predesessor
    currNode = root
    predesessor = None

    while (currNode):
        #Step1: currNode.left is None, we visit currNode and set currNode to its right child.
        if not currNode.left:
            print currNode.val
            currNode = currNode.right
            continue

        #Step2: currNode.left is not None, we find the predessesor of currNode
        predessesor = currNode.left
        while(predesessor.right):
            predessesor= predesessor.right

        #situation 2a)
        if not predesessor.right:
            predesessor.right = currNode
            currNode = currNode.left
            continue

        # situation 2b)
        # restore the structure of the tree
        predesessor.right = None
        print currNode.val
        currNode = currNode.right

    




    