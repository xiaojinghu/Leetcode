class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # the stack is used to store data
        self.stack = []
        # the top of the minstack is used to store the minimum so far
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # if there is no element in the stack, we just add them into the stack and the minstack
        if not self.stack:
            self.stack.append(x)
            self.min.append(x)
            return
        self.stack.append(x)
        if x<= self.min[-1]:
            self.min.append(min(x, self.min[-1]))
        return 

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if x==self.min[-1]:
            self.min.pop()
        return
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()