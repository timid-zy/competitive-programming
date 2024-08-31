class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1 
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            postfix *= nums[len(nums) - i]
            ans[i] *= prefix
            ans[len(nums) - i - 1] *= postfix
        
        return ans