# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        if not head or not head.next:
            return head
        
        curr = head
        nxt = head.next
        while nxt:
            curr.next = ListNode(gcd(curr.val, nxt.val), nxt)
            curr = nxt
            nxt = nxt.next
        
        return head