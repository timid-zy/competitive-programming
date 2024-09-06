# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_ = set(nums)
        d = ListNode(0, head)
        prev, curr = None, d
        while curr:
            if curr.val in set_:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
        
        return d.next