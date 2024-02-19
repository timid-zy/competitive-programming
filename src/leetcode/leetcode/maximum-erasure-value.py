class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        curr_score = 0
        max_score = 0
        seen_nums = {}

        for right in range(len(nums)):
            if nums[right] in seen_nums and seen_nums[nums[right]] >= left:
                max_score = max(max_score, curr_score)
                while left < seen_nums[nums[right]] + 1:
                    curr_score -= nums[left]
                    left += 1
            curr_score += nums[right]
            seen_nums[nums[right]] = right

        return max(max_score, curr_score)