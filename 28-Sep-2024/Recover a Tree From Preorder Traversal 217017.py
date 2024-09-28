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
        stk = {}
        while i < len(T):
            lvl = 0
            while i < len(T) and T[i] == "-":
                lvl += 1
                i += 1
            
            v = ""
            while i < len(T) and T[i] != "-":
                v += T[i]
                i += 1
            
            v = int(v)
            if lvl == 0:
                stk[0] = TreeNode(v)
                continue
            
            stk[lvl] = TreeNode(v)
            if stk[lvl-1].left is None:
                stk[lvl-1].left = stk[lvl]
            else:
                stk[lvl-1].right = stk[lvl]
            
        return stk[0]
            