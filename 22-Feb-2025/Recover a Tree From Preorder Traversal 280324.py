# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, T: str) -> Optional[TreeNode]:
        i = 0
        stk = []
        while i < len(T):
            lvl = 0
            while i < len(T) and T[i] == "-":
                lvl += 1
                i += 1
            
            j = i
            while i < len(T) and T[i] != "-":
                i += 1
            
            val = int(T[j:i])
            if lvl == 0:
                stk.append((TreeNode(val), lvl))
                continue
            
            while stk and stk[-1][1]+1 != lvl:
                stk.pop()
            
            node = TreeNode(val)
            if stk[-1][0].left is None:
                stk[-1][0].left = node
            else:
                stk[-1][0].right = node
            
            stk.append((node, lvl))
        
        return stk[0][0]