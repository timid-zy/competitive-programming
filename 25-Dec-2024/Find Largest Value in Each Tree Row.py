# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = [root.val]
        while queue:
            lvl_max = float('-inf')
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    lvl_max = max(lvl_max, curr.left.val)
                    queue.append(curr.left)
                
                if curr.right:
                    lvl_max = max(lvl_max, curr.right.val)
                    queue.append(curr.right)
            
            if lvl_max > float('-inf'):
                res.append(lvl_max)
        
        return res
        