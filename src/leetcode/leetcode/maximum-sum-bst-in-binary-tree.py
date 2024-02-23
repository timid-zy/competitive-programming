# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def checkBST(node, lowest, highest):
            if node is None:
                return 0
            
            if node.val >= highest or node.val <= lowest:
                return float('-inf')
            
            return node.val + checkBST(node.left, lowest, node.val) + checkBST(node.right, node.val, highest)
        
        max_sum = 0
        @cache
        def inorderTraversal(node, level=0):
            nonlocal max_sum
            if node is None:
                return None

            candidate = checkBST(node, float('-inf'), float('inf') )
            max_sum = max(max_sum, candidate)
            
            inorderTraversal(node.left)
            inorderTraversal(node.right)
            
            return max_sum
        
        return inorderTraversal(root)