# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def getRangeSum(node):
            if node is None:
                return 0
            
            if node.val < low or node.val > high:
                return getRangeSum(node.left) + getRangeSum(node.right)
            
            return node.val + getRangeSum(node.left) + getRangeSum(node.right)
        return getRangeSum(root)