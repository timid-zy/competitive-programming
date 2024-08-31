# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        pos_col = []
        neg_col = []
        
        def verticalBFS(node, row=0, col=0):
            if node is None:
                return
            
            if col >= 0 and col == len(pos_col):
                pos_col.append([])
            elif col < 0 and abs(col) - 1 == len(neg_col):
                neg_col.append([])
            
            if col >= 0:
                pos_col[col].append((node.val, row))
            else:
                neg_col[abs(col) - 1].append((node.val, row))
            
            verticalBFS(node.left, row + 1, col - 1)
            verticalBFS(node.right, row + 1, col + 1)

        verticalBFS(root)

        def getRow(arr): return (arr[1], arr[0])
        def getVal(arr): return arr[0]

        for p in pos_col:
            p.sort(key=getRow)
            for i in range(len(p)):
                p[i] = p[i][0]
        
        for n in neg_col: 
            n.sort(key=getRow)
            for i in range(len(n)):
                n[i] = n[i][0]
    
        return neg_col[::-1] + pos_col