# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(tree1, tree2):
            if not tree1 and not tree2:
                return None
            
            if tree1 and tree2:
                newNode = TreeNode()
                newNode.val = tree1.val + tree2.val
                newNode.left = merge(tree1.left, tree2.left)
                newNode.right = merge(tree1.right, tree2.right)
                return newNode
            
            return tree1 or tree2
        
        
        return merge(root1, root2)