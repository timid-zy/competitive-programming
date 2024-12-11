# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [(abs(c[0] - c[1]),i) for i, c in enumerate(costs)]
        diff.sort(reverse=True)
        nA = nB = 0
        res = 0
        for _, i in diff:
            if (nB == len(costs) // 2) or (costs[i][0] < costs[i][1] and nA < len(costs) // 2):
                nA += 1
                res += costs[i][0]
            else:
                nB += 1
                res += costs[i][1]
        
        return res
            
