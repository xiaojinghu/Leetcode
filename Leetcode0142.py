# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # this is the Floyd's Tortoise and Hare algorithm
        # Two steps:
        # 1. check if there is a cycle in the linked list, if there is no cycle, return None; else, return the meeting point of the two pointers
        #    set two pointers, slow and fast, and let them travel at the linked list. if they meet, then there is a cycle, if they do not meet, there is no cycle.
        # 2. find the entry of the cycle
        #    set ptr1 = meeting point, ptr2 = head; let ptr1 and ptr2 travel on the linked list at the same speed, when they meet, the node is the entry of the cycle.
        
        if not head or not head.next:
            return None
        # detect the cycle and find the meeting point
        slow = head
        fast = head
        # The flag is used to detect the cycle
        FLAG = -1
        # note the condition
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                FLAG = 1
                break
        if FLAG == -1:
            return None
        # find the entry of the cycle
        ptr1 = head
        ptr2 = slow
        while(ptr1!=ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
