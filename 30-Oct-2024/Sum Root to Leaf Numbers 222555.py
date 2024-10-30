# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node, par, val=0):
            if node is None:
                return val if par.left is None and par.right is None else 0
            
            return traverse(node.left, node, val * 10 + node.val) + traverse(node.right, node, val * 10 + node.val)
        
        return traverse(root, None) // 2