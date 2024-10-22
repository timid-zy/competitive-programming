# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            idx = nums[i] - 1
            if idx >= len(nums) or nums[i] <= 0 or nums[i] == nums[idx]:
                i += 1
                continue

            nums[i], nums[idx] = nums[idx], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
