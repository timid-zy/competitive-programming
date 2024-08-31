# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def findMax(node, max_, min_):
            nonlocal ans
            if not node: return None
            max_ = max(max_, node.val)
            min_ = min(min_, node.val)
            ans = max(ans, max_ - min_)
            findMax(node.left, max_, min_)
            findMax(node.right, max_, min_)
        
        ans = 0
        findMax(root, float('-inf'), float('inf'))
        return ans