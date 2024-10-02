# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, start: int, target: int) -> int:
        steps = 0
        curr = target
        while curr > start:
            if curr % 2 == 0:
                curr //= 2
            else:
                curr += 1
            
            steps += 1
            
        return steps + (start - curr)
