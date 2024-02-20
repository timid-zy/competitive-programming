class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count('R')
        d_count = senate.count('D')
        senate = deque(senate)
        r_del = 0
        d_del = 0
        
        
        while r_count > 0 and d_count > 0:
            sen = senate[0]
            if sen == "R" and r_del > 0:
                senate.popleft()
                r_count -= 1
                r_del -= 1
            
            elif sen == "R" and r_del == 0:
                sen = senate.popleft()
                senate.append(sen)
                d_del += 1
            
            elif sen == "D" and d_del > 0:
                senate.popleft()
                d_del -= 1
                d_count -= 1
            
            elif sen == "D" and d_del == 0:
                sen = senate.popleft()
                senate.append(sen)
                r_del += 1

        return "Radiant" if d_count == 0 else "Dire"