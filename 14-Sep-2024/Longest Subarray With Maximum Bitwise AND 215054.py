# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = res = 0
        max_num = max(nums)
        for i in range(len(nums)):
            if nums[i] == max_num:
                curr += 1
                res = max(curr, res)
            else:
                curr = 0

        return res
        