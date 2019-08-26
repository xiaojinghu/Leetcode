# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):  
    def merge2Lists(self, p, q):
        if not p:
            return q
        if not q:
            return p
        dummyHead = ListNode(0)
        dummy = dummyHead
        while(p and q):
            if p.val<=q.val:
                # we append p in the dummy list
                dummy.next = p
                p = p.next
                dummy = dummy.next
                dummy.next = None
                continue
            dummy.next = q
            q = q.next
            dummy = dummy.next
            dummy.next = None
        if p:
            dummy.next = p
        if q:
            dummy.next = q
        return dummyHead.next
                
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        
        leftPart = lists[:len(lists)/2+1]
        rightPart = lists[len(lists)/2+1:]
        return self.merge2Lists(self.mergeKLists(leftPart), self.mergeKLists(rightPart))