# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean*(n + len(rolls)) - sum(rolls)
        if target / n > 6 or target / n < 1:
            return []
        
        missing = [0] * n
        sub = target // n
        for i in range(n):
            missing[i] = sub
            target -= sub
        
        i = 0
        while target > 0:
            missing[i] += 1
            i += 1
            target -= 1
        
        return missing
