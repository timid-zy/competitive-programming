# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        
        count = 1
        p1 = head.next
        p2 = head.next.next

        while p1:
            prev_val = p1.val
            curr = p1
            next = curr.next
            
            i = 0
            while next and i < count:
                temp = next.val
                next.val = prev_val
                prev_val = temp

                curr = curr.next
                next = next.next
                i += 1
            
            p1.val = prev_val
            p1 = p1.next
            count += 1

            for i in range(2):
                p2 = p2.next
                if p2 is None:
                    return head

        return head
