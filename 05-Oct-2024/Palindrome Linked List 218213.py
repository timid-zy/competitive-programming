# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        stk = []
        curr = head
        while curr != slow:
            stk.append(curr.val)
            curr = curr.next
        
        if fast is not None:
            slow = slow.next
        
        while slow:
            if stk.pop() != slow.val:
                return False
            
            slow = slow.next
        
        return True
