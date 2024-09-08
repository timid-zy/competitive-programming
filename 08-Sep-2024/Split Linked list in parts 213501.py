# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l, curr = 0, head
        while curr: l += 1; curr = curr.next

        res = [None] * k
        d = l // k
        curr = head
        for i in range(len(res)):
            r = l % k
            count = d + 1 if r > 0 else d
            l -= count
            k -= 1
            local_curr = res[i] = ListNode()
            for _ in range(count):
                local_curr.next = curr
                local_curr = local_curr.next
                curr = curr.next
            
            local_curr.next = None
            res[i] = res[i].next
        
        return res
