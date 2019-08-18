# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        integer = ''
        for char in s:
            # print stack
            if char == ',':
                if integer:
                    stack.append(NestedInteger(int(integer)))
                    integer = ''
                continue
            if char == '[':
                if integer:
                    stack.append(NestedInteger(int(integer)))
                    integer = ''
                stack.append(char)
                continue
            if char.isdigit() or char == '-':
                integer += char
                continue
            # print stack
            if char == ']':
                if integer:
                    stack.append(NestedInteger(int(integer)))
                    integer = ''
                node = NestedInteger()
                elemList = []
                while(stack and stack[-1]!='['):
                    elemList.append(stack.pop())
                stack.pop()
                while(elemList):
                    node.add(elemList.pop())
                stack.append(node)
                # print stack
                continue
                    
        if integer:
            #this means s is a single integer
            return NestedInteger(int(integer))
        return  stack[0]