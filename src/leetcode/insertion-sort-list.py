# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr1 = head.next
        while curr1:

            curr2 = curr1
            key = curr2.val

            start = head
            while key >= start.val and start != curr2:
                start = start.next
            
            while start != curr2:
                temp = start.val
                start.val = key
                key = temp
                start = start.next
            
            curr2.val = key
            curr1 = curr1.next

        return head