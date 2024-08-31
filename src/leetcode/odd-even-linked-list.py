# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odd_head = head.next
        even = head
        odd = head.next

        while even and odd:
            even.next = odd.next
            if even.next is None:
                break
            even = odd.next
            odd.next = even.next
            odd = even.next

        if odd is not None:
            odd.next = None
        even.next = odd_head

        return head