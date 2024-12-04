# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(node):
            prev = None
            slow = fast = node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if fast is None:
                return prev
            
            return slow
    
        def mergeSort(node):
            if node is None or node.next is None:
                return node
            
            mid = getMid(node)
            nxt = mid.next
            mid.next = None
            left = mergeSort(node)
            right = mergeSort(nxt)

            return merge(left, right)
        
        def merge(list1, list2):
            res = c = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    c.next = list1
                    list1 = list1.next
                    c = c.next
                    c.next = None
                else:
                    c.next = list2
                    list2 = list2.next
                    c = c.next
                    c.next = None
            
            if list1:
                c.next = list1
            if list2:
                c.next = list2
            
            return res.next
        
        return mergeSort(head)