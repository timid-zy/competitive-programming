# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        B = [0, 0]
        for b in bills:
            if b == 5: B[0] += 1
            elif b == 10 and B[0] > 0:
                B[0] -= 1
                B[1] += 1
            elif b == 20 and B[0] > 0 and B[1] > 0:
                B[1] -= 1
                B[0] -= 1
            elif b == 20 and B[0] > 2: B[0] -= 3
            else: return False
        
        return True