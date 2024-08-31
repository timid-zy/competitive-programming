# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        nextN = head.next

        while nextN:
            actualNext = nextN.next
            curr.next = prev
            nextN.next = curr

            prev = curr
            curr = nextN
            nextN = actualNext
        
        return curr