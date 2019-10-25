class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = collections.deque(v1)
        self.v2 = collections.deque(v2)
        if not v1:
            self.v1, self.v2 = self.v2, self.v1

    def next(self):
        """
        :rtype: int
        """
        # print self.v1, self.v2
        if len(self.v1)>0:
            num = self.v1.popleft()
        if len(self.v2)>0:
            self.v1, self.v2 = self.v2, self.v1 
        return num
           

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v1)>0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())