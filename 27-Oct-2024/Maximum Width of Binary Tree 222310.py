# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(0, root)])
        res = 0
        while queue:
            mn, mx = float('inf'), float('-inf')
            for _ in range(len(queue)):
                i, curr = queue.popleft()
                if curr is None:
                    continue
                
                mn = min(mn, i)
                mx = max(mx, i)
                queue.append((2*i, curr.left))
                queue.append((2*i + 1, curr.right))
            
            if mn < float('inf'):
                res = max(res, mx - mn + 1)
        
        return res

