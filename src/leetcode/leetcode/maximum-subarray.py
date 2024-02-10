class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        r_sum = 0

        for i in range(len(nums)):
            r_sum = max(r_sum, 0)
            r_sum += nums[i]
            max_sum = max(max_sum, r_sum)
        
        return max_sum