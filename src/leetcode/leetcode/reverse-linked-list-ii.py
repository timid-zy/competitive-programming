# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        right_el = None
        left_el = None
        right_edge = None
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            if list_len == right:
                right_el = curr
                if curr.next:
                    right_edge = curr.next
            if list_len == left:
                left_el = curr
            curr = curr.next
        
        left_edge = None
        if left > 1:
            left_edge = head
            for i in range(left - 2):
                left_edge = left_edge.next
        
        curr = left_el
        next = left_el.next
        while curr != right_el:
            actual_next = next.next
            next.next = curr

            curr = next
            next = actual_next

        if left_edge:
            left_edge.next = right_el
        if right_edge:
            left_el.next = right_edge
        if not left_edge and not right_edge:
            left_el.next = None
            return right_el
        if not left_edge:
            return right_el
        if not right_edge:
            left_el.next = None
            return head
        
        
        return head