# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = 0
        jobs = sorted(list(zip(profit, difficulty)))
        worker.sort()
        r = len(jobs)-1
        for a in reversed(worker):
            while r >= 0 and a < jobs[r][1]:
                r -= 1
            
            if r == -1: break
            res += jobs[r][0]
        
        return res