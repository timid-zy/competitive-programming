# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.val < x:
            curr = curr.next
        if curr is None:
            return head
        
        pointer1 = curr.next
        pointer2 = curr

        while pointer1:
            if pointer1.val < x:
                curr = pointer2
                next = curr.next
                prev_val = curr.val

                while curr != pointer1:
                    temp = next.val
                    next.val = prev_val
                    prev_val = temp

                    curr = curr.next
                    next = next.next
                pointer2.val = prev_val
                pointer2 = pointer2.next
            pointer1 = pointer1.next
        
        return head