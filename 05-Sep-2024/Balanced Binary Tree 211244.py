# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node is None:
                return 0, True
            
            left, lans = solve(node.left)
            right, rans = solve(node.right)
            return max(left, right) + 1, lans & rans & (abs(left-right) <= 1)
        
        return solve(root)[1]
