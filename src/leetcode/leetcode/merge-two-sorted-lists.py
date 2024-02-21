# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeTwo(tail, list1, list2):
            if not list1 and not list2:
                return tail

            if list2 and (not list1 or list1.val > list2.val):
                nextEl = ListNode(list2.val)
                tail.next = nextEl
                tail = tail.next
                list2 = list2.next
            else:
                nextEl = ListNode(list1.val)
                tail.next = nextEl
                tail = tail.next
                list1 = list1.next
            
            return mergeTwo(tail, list1, list2)

        head = None
        if list1 is None and list2 is None:
            return None

        if list2 and (not list1 or list1.val > list2.val):
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        head.next = None
        mergeTwo(head, list1, list2)
        return head