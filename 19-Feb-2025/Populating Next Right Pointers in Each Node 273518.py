# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if not root:
        #     return root

        # queue = deque([root])
        # while queue:
        #     n = len(queue)
        #     for i in range(n):
        #         curr = queue.popleft()
        #         if i < n-1:
        #             curr.next = queue[0]
                
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        
        # return root
        head = root
        while head and head.left:
            curr = head
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next
            
            head = head.left
        
        return root
                


