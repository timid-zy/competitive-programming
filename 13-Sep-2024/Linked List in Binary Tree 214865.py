# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

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
        def traverse(tn, ln):
            if tn is None or ln is None:
                return ln is None 
            
            if tn.val != ln.val:
                return False

            return traverse(tn.left, ln.next) or traverse(tn.right, ln.next)
        
        def solve(rt, hd):
            if rt is None:
                return hd is None
                
            if traverse(rt, hd):
                return True
            
            return solve(rt.left, hd)  or solve(rt.right, hd)
        
        return solve(root, head)
