# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx):
            if sum(curr) > target or idx == len(candidates):
                return

            if sum(curr) == target:
                res.append(curr[:])
                return
            
            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                backtrack(i)
                curr.pop()
        
        curr = []
        res = []
        backtrack(0)
        return res