# Problem: Sliding Puzzle - https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def check_end(self, b):
        return b[0][0] == 1 and b[0][1] == 2 and b[0][2] == 3 and b[1][0] == 4 and b[1][1] == 5 and b[1][2] == 0
    
    def get_neighbors(self, b):
        zr, zc = 0, 0
        if 0 in b[1]:
            zr = 1
        
        zc = b[zr].index(0)
        res = []
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = zr + dr, zc + dc
            if 0 <= nr <= 1 and 0 <= nc <= 2:
                newb = [b[0][::], b[1][::]]
                newb[zr][zc], newb[nr][nc] = newb[nr][nc], newb[zr][zc]
                res.append(newb)
        
        return res


    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque([(board, 0)])
        visited = set([tuple(board[0] + board[1])])
        while queue:
            b, v = queue.popleft()
            if self.check_end(b):
                return v
            
            for nb in self.get_neighbors(b):
                k = tuple(nb[0] + nb[1])
                if k not in visited:
                    visited.add(k)
                    queue.append((nb, v+1))
        
        return -1