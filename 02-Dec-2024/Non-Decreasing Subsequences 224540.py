# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if len(curr) >= 2:
                res.add(tuple(curr[:]))
            
            for j in range(i+1, len(nums)):
                if len(curr) == 0 or curr[-1] <= nums[j]:
                    curr.append(nums[j])
                    backtrack(j)
                    curr.pop()
        
        curr = []
        res = set()
        backtrack(-1)
        return list(res)