# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
        lenB = 0
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next

        diff = abs(lenB - lenA)

        
        if lenA > lenB:
            for i in range(diff):
                headA = headA.next
        else:
            for i in range(diff):
                headB = headB.next
        

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next