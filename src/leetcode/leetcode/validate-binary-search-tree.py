# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, lowest, highest):
            if node is None:
                return True
            
            if node.val >= highest or node.val <= lowest:
                return False
            
            return validateBST(node.left, lowest, node.val) and validateBST(node.right, node.val, highest)

        return validateBST(root, float('-inf'), float('inf'))