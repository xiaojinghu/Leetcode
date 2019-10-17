class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.Peek = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.Peek is None:
            self.Peek = x
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        buf = []
        for i in range(len(self.stack)-1):
            buf.append(self.stack.pop())
        x =  self.stack.pop()
        if not buf:
            self.Peek = None
            return x
        else:
            self.Peek = buf[-1]
            while(buf):
                self.stack.append(buf.pop())
        return x
            

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.Peek

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
