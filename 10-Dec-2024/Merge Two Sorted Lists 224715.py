# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c = dummy = ListNode()

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                c.next = curr1
                c = c.next
                curr1 = curr1.next
            else:
                c.next = curr2
                c = c.next
                curr2 = curr2.next
        
        while curr1:
            c.next = curr1
            curr1 = curr1.next
            c = c.next
        
        while curr2:
            c.next = curr2
            curr2 = curr2.next
            c = c.next
        
        return dummy.next