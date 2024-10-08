# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def validate(x, y, arr):
            return 0 <= x < m and 0 <= y < n and arr[x][y] == -1

        res = [[-1] * n for _ in range(m)]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        r = c = 0
        curr = head
        while True:
            res[r][c] = curr.val
            curr = curr.next
            if curr is None:
                break
            
            while not validate(r + d[di][0], c + d[di][1], res):
                di = (di + 1) % 4
            
            r += d[di][0]
            c += d[di][1]
        
        return res
        