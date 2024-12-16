# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = 0
        mx = float('-inf')
        for i in range(len(nums)):
            if rs < 0: rs = 0
            rs += nums[i]
            mx = max(rs, mx)

        return mx