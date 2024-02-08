class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # -2 -1 -4 0 -1 1 2 -4 0
        r_sum = nums[0]
        min_sum = min(0, nums[0])
        max_sum = nums[0]

        for i in range(1, len(nums)):
            r_sum += nums[i]
            max_sum = max(max_sum, r_sum - min_sum)
            min_sum = min(min_sum, r_sum)
        
        return max_sum

