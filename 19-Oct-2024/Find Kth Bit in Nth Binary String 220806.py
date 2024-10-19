# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ub = 1
        while k > ub:
            ub *= 2
            ub += 1
        
        revs = 0
        while k > 1:
            mid = ub // 2 + 1
            if k == mid:
                return "1" if revs == 0 else "0"
            elif k < mid:
                ub -= 1
                ub //= 2
            else:
                revs = (revs + 1) % 2
                k = ub - k + 1

        return "0" if revs == 0 else "1"