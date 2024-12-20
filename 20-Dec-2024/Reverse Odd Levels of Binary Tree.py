# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        lvl = 0
        while queue:
            nbs = []
            for _ in range(len(queue)):
                c = queue.popleft()
                if lvl % 2:
                    nbs.append(c)
                
                if c.left and c.right:
                    queue.append(c.left)
                    queue.append(c.right)
            
            i, j = 0, len(nbs) - 1
            while i < j:
                nbs[i].val, nbs[j].val = nbs[j].val, nbs[i].val
                i += 1
                j -= 1
    
            lvl += 1
        
        return root