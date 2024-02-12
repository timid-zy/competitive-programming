# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        last = head
        curr = head

        for i in range(n):
            last = last.next
        
        # to delete the first element
        if not last:
            if curr.next:
                return curr.next
            else:
                return None
        
        while last.next:
            last = last.next
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head