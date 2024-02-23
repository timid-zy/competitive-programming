# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        def bst(node, level=0):
            if node is None: return None

            if len(arr) == level:
                arr.append([])
            arr[level].append(node.val)
            bst(node.left, level + 1)
            bst(node.right, level + 1)
        
        bst(root)
        for i in range(1, len(arr), 2):
            arr[i] = arr[i][::-1]
        return arr

