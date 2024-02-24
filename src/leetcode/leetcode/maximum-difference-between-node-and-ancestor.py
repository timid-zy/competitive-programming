# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        @lru_cache
        def getEdges(node):
            if node is None:
                return float('inf'), float('-inf')

            mnl, mxl = getEdges(node.left)
            mnr, mxr = getEdges(node.right)
            
            return (
                min(node.val, mnl, mnr),
                max(node.val, mxl, mxr)
            )
            
        @lru_cache
        def maxAncestor(node):
            if node is None or (node.left is None and node.right is None):
                return float('-inf')
            
            mn, mx = getEdges(node)
            
            return max(
                abs(node.val - mn),
                abs(node.val - mx),
                maxAncestor(node.left),
                maxAncestor(node.right)
            )
            
        return maxAncestor(root)