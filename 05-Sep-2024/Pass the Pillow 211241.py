# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        di, rem = divmod(time, n-1)
        return rem + 1 if di % 2 == 0 else n - rem