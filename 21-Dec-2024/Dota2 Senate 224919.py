# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        curr = 0
        while queue:
            nr = nc = 0
            for _ in range(len(queue)):
                c = queue.popleft()
                if (c == 'R' and curr < 0) or (c == 'D' and curr > 0):
                    curr = (abs(curr) - 1) * abs(curr) // curr
                    continue
                
                queue.append(c)
                if c == 'R':
                    nr += 1
                    curr += 1
                else:
                    nc += 1
                    curr -= 1
                
            if nr == 0: return "Dire"
            if nc == 0: return "Radiant" 