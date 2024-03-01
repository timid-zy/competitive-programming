# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def inorderBST(node):
            nonlocal arr
            if node is None:
                return

            inorderBST(node.left)
            arr.append(node.val)
            inorderBST(node.right)
        
        inorderBST(root)

        def constructBST(left, right):
            nonlocal arr
            if left > right:
                return None
            
            midPoint = (right + left + 1) // 2

            return TreeNode(
                arr[midPoint],
                constructBST(left, midPoint - 1),
                constructBST(midPoint + 1, right)
            )


        return constructBST(0, len(arr) - 1)