# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        is_cycle = False
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p2 == p1:
                is_cycle = True
                break
            
        if not is_cycle:
            return None
        
        p1 = head
        count = 0
        while True:
            if p2 == p1: return p2
            p1 = p1.next
            p2 = p2.next            