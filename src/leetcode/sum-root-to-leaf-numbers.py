# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sum_ = 0
        
        def dfs(node, curr=""):
            nonlocal sum_
            if node is None:
                if curr == "": return
                sum_ += int(curr)
                return
            
            if node.left and not node.right:
                dfs(node.left, curr + str(node.val))
            elif node.right and not node.left:
                dfs(node.right, curr + str(node.val))
            else:
                dfs(node.left, curr + str(node.val))
                dfs(node.right, curr + str(node.val))

        
        dfs(root)
        return sum_ // 2