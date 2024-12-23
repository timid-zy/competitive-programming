# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        op = 0
        while queue:
            res = list(map(lambda x: x.val, queue))
            sres = sorted(res)
            dct = {sres[i]: i for i in range(len(sres))}
            
            for i in range(len(res)):
                t = dct[res[i]]
                while i != t:
                    res[i], res[t] = res[t], res[i]
                    op += 1
                    t = dct[res[i]]

            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return op 