from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = 0
        self.Top = None
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.size += 1
        self.Top = x
        return
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.size == 1:
            self.Top = None
            self.size = 0
            return self.queue.popleft()
        for i in range(self.size-1):
            x = self.queue.popleft()
            self.queue.append(x)
            self.Top = x
        self.size -= 1
        return self.queue.popleft()
    

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.Top
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size == 0
            
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()