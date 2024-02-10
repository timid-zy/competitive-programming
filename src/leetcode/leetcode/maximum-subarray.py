class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r_sum = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            if r_sum < 0:
                r_sum = 0
            r_sum += nums[i]
            max_sum = max(r_sum, max_sum)
        
        return max_sum