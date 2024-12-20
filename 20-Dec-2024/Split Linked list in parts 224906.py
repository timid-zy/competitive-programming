# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ln, curr = 0, head
        while curr:
            ln += 1
            curr = curr.next

        res = [None] * k
        d = ln // k
        curr = head
        for i in range(len(res)):
            r = ln % k
            count = d + 1 if r > 0 else d
            ln -= count
            k -= 1
            lcurr = res[i] = ListNode()
            for _ in range(count):
                lcurr.next = curr
                lcurr = lcurr.next
                curr = curr.next
            
            lcurr.next = None
            res[i] = res[i].next
        
        return res
