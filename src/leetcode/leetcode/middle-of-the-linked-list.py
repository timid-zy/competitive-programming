# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 1
        curr = head
        while curr.next:
            list_len += 1
            curr = curr.next
        
        curr = head
        for i in range(list_len // 2):
            curr = curr.next
        return curr

        