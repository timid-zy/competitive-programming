# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr: n += 1; curr = curr.next

        i = 0
        nk = n - k + 1
        f = None
        curr = head
        while curr:
            i += 1
            if (k < nk and i == k) or (nk < k and i == nk):
                f = curr
            elif (k < nk and i == nk) or (nk < k and i == k):
                curr.val, f.val = f.val, curr.val
                break
            
            curr = curr.next
        
        return head