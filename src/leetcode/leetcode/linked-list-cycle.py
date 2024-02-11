# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        count = 1 
        while head.next:
            count += 1
            head = head.next
            if count > 10000: # maximum length in constraints
                return True
        
        return False