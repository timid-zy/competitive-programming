class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        return prefix_sum