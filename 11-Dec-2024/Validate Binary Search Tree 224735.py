# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def check(node):
        #     nonlocal ans
        #     lmn, lmx = float('inf'), float('-inf')
        #     rmn, rmx = float('inf'), float('-inf')
        #     if node.left:
        #         lmn, lmx = check(node.left)
        #     if node.right:
        #         rmn, rmx = check(node.right)
            
        #     if lmx >= node.val or node.val >= rmn:
        #         ans = False
            
        #     return min(lmn, rmn, node.val), max(lmx, rmx, node.val)

        # ans = True
        # check(root)
        # return ans

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        arr = []
        inorder(root)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False

        return True