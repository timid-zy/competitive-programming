# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # calculate length
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        
        arr = [ None for i in range(k)]
        if list_len <= k:
            curr = head
            i = 0 
            while curr:
                arr[i] = ListNode(curr.val)
                curr = curr.next
                i += 1
            return arr
        else:
            val = list_len // k
            arr = [val] * k
            
            i = 0
            remainder = list_len % k
            while remainder > 0:
                arr[i] += 1
                remainder -= 1
                i += 1

        prev_head = head
        for i in range(len(arr)):
            curr = prev_head
            for j in range(arr[i] - 1):
                curr = curr.next
            arr[i] = prev_head
            prev_head = curr.next
            curr.next = None
        
        return arr