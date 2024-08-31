class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        sub_sum = 0
        min_len = len(nums) + 1
        for end in range(len(nums)):
            sub_sum += nums[end]
            while sub_sum >= target:
                # print(start, end)
                min_len = min(min_len, end - start + 1)
                sub_sum -= nums[start]
                start += 1
        
        return min_len if min_len <= len(nums) else 0