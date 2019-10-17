# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        # each time we append the smallest node from lists
        # we just need tro choose the smallest from each starting node from each sorted list
        minHeap = []
        # initialize the min-heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val,lists[i]))
        dummyHead = ListNode(0)
        p = dummyHead
        while(minHeap):
            # pop out the minimum
            minNode = heapq.heappop(minHeap)[1]
            # get the next node of minNode and push it into the heap
            nextNode = minNode.next
            if nextNode:
                heapq.heappush(minHeap, (nextNode.val, nextNode))
            # add the minNode to the dummy head
            p.next = minNode
            p = p.next
            p.next = None
        return dummyHead.next
            
