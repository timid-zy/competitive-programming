# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def backtrack(i, prev_sum):
            if i == len(nums):
                return 1 if prev_sum == target else 0
            
            return backtrack(i+1, prev_sum + nums[i]) + backtrack(i+1, prev_sum - nums[i])
        
        return backtrack(0, 0)