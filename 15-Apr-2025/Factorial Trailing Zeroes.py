class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        b = 5
        while b <= n:
            fives += n // b
            b *= 5

        return fives