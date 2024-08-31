# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        max_ = 0
        if root:
            queue.append((root, 1))
            max_ = 1
        
        while len(queue) > 0:
            least = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr[0] is None: continue
                if not least:
                    least = curr[1]
                else:
                    max_ = max(max_, curr[1] - least + 1)
                
                queue.append((curr[0].left, curr[1] * 2 - 1))
                queue.append((curr[0].right, curr[1] * 2))
        
        return max_