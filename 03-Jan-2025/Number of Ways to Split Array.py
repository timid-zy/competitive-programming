class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        cs, res = nums[-1], 0
        for i in range(len(nums)-2, -1, -1):
            if prefix[i] >= cs:
                res += 1

            cs += nums[i]
        
        return res