class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        icecream_bought = 0
        curr_coins = coins
        for i in range(len(sorted_costs)):
            if curr_coins >= sorted_costs[i]:
                icecream_bought += 1
                curr_coins -= sorted_costs[i]
        return icecream_bought