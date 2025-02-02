# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) + 1)
        for n in costs:
            counts[n] += 1

        cnt = 0
        for i in range(len(counts)):
            if counts[i] == 0:
                continue
                        
            bs = min(counts[i], coins // i)
            coins -= bs * i
            cnt += bs
            print(bs, i)
        
        return cnt