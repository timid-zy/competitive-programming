# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def constructTree(left, right):
            if left > right:
                return None
            
            max_idx = left
            for i in range(left, right + 1):
                if nums[max_idx] < nums[i]:
                    max_idx = i
            
            node = TreeNode(
                nums[max_idx],
                constructTree(left, max_idx - 1),
                constructTree(max_idx + 1, right)
            )
            return node
        
        return constructTree(0, len(nums) - 1)