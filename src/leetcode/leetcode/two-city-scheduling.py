class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        def getProfit(arr):
            return arr[1] - arr[0]
        
        costs.sort(key=getProfit)
        min_cost = 0
        mid_point = len(costs) // 2
        for i in range(len(costs)):
            if i < mid_point:
                min_cost += costs[i][1]
            else:
                min_cost += costs[i][0]
            
        return min_cost