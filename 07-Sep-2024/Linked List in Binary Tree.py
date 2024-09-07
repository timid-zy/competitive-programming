# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def solve(node, curr):
            nonlocal res
            if node is None or curr is None:
                return

            nxt = curr.next if node.val == curr.val else head.next if node.val == head.val else head
            if nxt is None:
                res = True
                return 

            solve(node.left, nxt)
            solve(node.right, nxt)
            if nxt != head and node.val == head.val:
                solve(node.left, head.next)
                solve(node.right, head.next)

        res = False; solve(root, head); return res