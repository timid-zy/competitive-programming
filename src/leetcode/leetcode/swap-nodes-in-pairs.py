# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head
        next = head.next
        head = next

        while curr and curr.next:
            actualNext = next.next
            curr.next = actualNext
            next.next = curr
            if prev:
                prev.next = next
            prev = curr
            curr = curr.next
            if curr: 
                next = curr.next
    
        return head