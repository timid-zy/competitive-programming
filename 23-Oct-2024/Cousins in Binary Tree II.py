# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_val(node, depth=0):
            if node is None:
                return 0
            
            memo[node] = node.val
            lvl[depth] += node.val
            get_val(node.left, depth+1); get_val(node.right, depth+1)
            return memo[node]
        
        def traverse(node, par, depth=0):
            if node is None:
                return
            
            node.val = 0
            if par and depth > 1:
                node.val = lvl[depth] - memo[par.left] - memo[par.right]

            traverse(node.left, node, depth + 1); traverse(node.right, node, depth + 1)
            
        
        memo = {None: 0}
        lvl = defaultdict(int)
        get_val(root); traverse(root, None)
        return root
