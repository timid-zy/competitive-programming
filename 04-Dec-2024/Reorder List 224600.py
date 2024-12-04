# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, node):
        prev = None; slow = fast = node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast is None:
            return prev
        return slow
    
    def reverse(self, node):
        prev = None; curr = node
        while curr != None:
            nx = curr.next
            curr.next = prev
            prev = curr
            curr = nx
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.getMid(head)
        nx = mid.next
        mid.next = None
        list2 = self.reverse(nx)
        list1 = head
        while list1 and list2:
            nx1 = list1.next
            list1.next = list2
            nx2 = list2.next
            list2.next = nx1
            list1 = nx1
            list2 = nx2

        return head