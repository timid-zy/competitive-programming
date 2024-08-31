# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict1 = {}
        
        def countNodes(node):
            if node is None:
                return None
            
            dict1[node.val] = dict1.get(node.val, 0) + 1
            countNodes(node.left)
            countNodes(node.right)

        countNodes(root)

        max_nums = []
        max_count = 0
        print(dict1)
        for num in dict1:
            count = dict1[num]
            if count > max_count:
                max_count = count
                max_nums = [num]
            elif count == max_count:
                max_nums.append(num)
        
        return max_nums