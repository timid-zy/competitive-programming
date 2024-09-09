# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def inbound(x, y, grid):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[-1] * n for _ in range(m)]
        r = c = di = 0
        curr = head
        while curr:
            res[r][c] = curr.val
            curr = curr.next
            nr, nc = r + dire[di][0], c + dire[di][1]
            if not inbound(nr, nc, res) or res[nr][nc] != -1:
                di = (di + 1) % 4
            
            r, c = r + dire[di][0], c + dire[di][1]
        
        return res
        