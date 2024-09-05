# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, P: List[int]) -> int:
        res = 1
        cont = 1
        for i in range(1, len(P)):
            if P[i-1] == P[i] + 1:
                cont += 1
            else:
                cont = 1
            
            res += cont

        return res