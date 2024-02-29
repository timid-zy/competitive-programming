# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def toBST(left, right):
            if left > right:
                return
            
            midPoint = (left + right) // 2
            node = TreeNode(nums[midPoint])
            node.left = toBST(left, midPoint - 1)
            node.right = toBST(midPoint + 1, right)
            return node
            
        return toBST(0, len(nums) - 1)