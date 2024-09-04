# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        v = pow(2, n, 10 ** 9 + 7) - 2
        return v if v >= 0 else 10 ** 9 + 7 + v