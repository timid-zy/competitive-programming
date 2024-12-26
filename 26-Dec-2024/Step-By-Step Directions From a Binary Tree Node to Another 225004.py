# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_path(node, dest, path):
            if node is None: return False
        
            if node.val == dest: return True
            
            path.append("L")
            if get_path(node.left, dest, path): return True
            
            path[-1] = "R"
            if get_path(node.right, dest, path): return True
            
            path.pop()
            return False
        
        p1, p2 = [], []
        get_path(root, startValue, p1)
        get_path(root, destValue, p2)
        i = j = 0
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                i += 1; j += 1
            else:
                break

        return "U" * (len(p1) - i) + "".join(p2[j:])
            