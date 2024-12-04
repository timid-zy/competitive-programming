# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        for i in range(1, n):
            res += [2**i + res[j] for j in range(len(res)-1,-1,-1)]
        
        return res
