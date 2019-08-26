# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            # no duplicates
            return head
        
        # set a dummpy head
        dummy = ListNode(0)
        p = dummy
        q = head
        while(q):            
            k = q
            while(k.next):
                if k.next.val == q.val:
                    k = k.next
                else:
                    break
            if k == q:
                 # then there must be no duplicate for q
                # we append q to the dummy head List
                p.next = q
                q = q.next
                p = p.next
                p.next = None 
                continue
            # now k pointsd to the last duplicate of q
            # we need to skip these duplicates
            q = k.next
        return dummy.next