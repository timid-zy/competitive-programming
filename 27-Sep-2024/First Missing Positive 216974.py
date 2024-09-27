# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[nums[i] - 1] == nums[i]:
                i += 1; continue
            
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(1, len(nums) + 1):
            if nums[i - 1] != i:
                return i
        
        return len(nums) + 1