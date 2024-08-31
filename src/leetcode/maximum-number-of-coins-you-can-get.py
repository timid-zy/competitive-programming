class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles_sorted = sorted(piles)
        max_coins = 0
        max_takes = len(piles) // 3
        i = len(piles) - 2
        piles_taken = 0
        while i >= 0 and piles_taken < max_takes:
            max_coins += piles_sorted[i]
            i -= 2
            piles_taken += 1
        return max_coins

        # 1 2 3 4 5 6 7 8 9
        # 1 8 9
        # 2 