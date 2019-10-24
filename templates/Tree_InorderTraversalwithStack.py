# inorder traversal of a tree using stack

def inorder(root):
    if not root:
        return  None

    # Initialization of the stack
    stack = [root]

    while(stack):
        # Step1: if the current top element has a left child, we push it into the stack:
        #        if the current top element has no left child, we go to Step2
        while(stack and stack[-1].left):
            stack.append(stack[-1].left)
            continue

        # Step2: if the stack is not empty, we pop the top element out. if it do not has
        #        a right child, we repeat Step2, else, we jump to Step1.
        while(stack):
            node = stack.pop()
            if not node.right:
                continue
            stack.append(node.right)
            break



        


