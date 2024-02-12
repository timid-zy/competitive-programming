# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        curr = headA
        while curr:
            nodes.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            pre_len = len(nodes)
            nodes.add(curr)
            if pre_len == len(nodes):
                return curr
            curr = curr.next
        
        return None