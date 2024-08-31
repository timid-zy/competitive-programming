# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        if head.next is None:
            return True

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        
        first = head
        second = slow_p

        stack = []
        while slow_p:
            stack.append(first.val)
            slow_p = slow_p.next
            first = first.next

        while second:
            if second.val != stack.pop():
                return False
            second = second.next
        return True