# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr != None:
            if prev is not None and prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return head