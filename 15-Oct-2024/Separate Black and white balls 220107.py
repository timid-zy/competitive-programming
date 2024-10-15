# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroes = swaps = 0
        for c in reversed(s):
            if c == "0":
                zeroes += 1
            else:
                swaps += zeroes
        
        return swaps