# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            return None if head.val == head.next.val else head
        
        prev = None
        slow = head
        fast = head.next

        while fast:
            if slow.val == fast.val:
                while fast and slow.val == fast.val:
                    fast = fast.next
                if slow == head:
                    head = fast
                    slow = fast
                    fast = fast.next if fast else None
                else:
                    prev.next = fast
                    slow = fast
                    fast = fast.next if fast else None

            else:
                prev = slow
                slow = slow.next
                fast = fast.next
        
        return head