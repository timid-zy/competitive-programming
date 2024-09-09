# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            c = 0
            for j in range(17, -1, -1):
                if i & (1 << j): c += 1
            
            res.append(c)
        
        return res