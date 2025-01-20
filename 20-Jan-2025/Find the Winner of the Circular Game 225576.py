# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def rec(at):
            nonlocal n, k
            if len(lost) == n-1:
                return list(set(range(1, n+1)) - lost)[0]
            
            ck = k
            curr = at
            while ck > 0:
                if curr not in lost:
                    ck -= 1
                    if ck == 0:
                        lost.add(curr)
                
                curr += 1
                if curr > n: curr = 1
            
            return rec(curr)
        
        lost = set()
        return rec(1)