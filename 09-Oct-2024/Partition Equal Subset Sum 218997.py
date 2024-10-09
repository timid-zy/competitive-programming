# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i, sum_):
            if sum_ == total // 2:
                return True

            if i == len(nums):
                return False
            
            return dp(i+1, sum_ + nums[i]) or dp(i+1, sum_)

        total = sum(nums)
        if total % 2 == 1:
            return False
        
        return dp(0, 0)
        