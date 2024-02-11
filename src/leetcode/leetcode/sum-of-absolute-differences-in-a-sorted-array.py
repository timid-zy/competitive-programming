class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            postfix[len(nums) - 1 - i] = postfix[len(nums) - i] + nums[len(nums) - i]
        
        ans = [0] * len(nums)
        for i in range(len(ans)):
            ans[i] = nums[i]*i - prefix[i] + postfix[i] - nums[i]*(len(nums) - 1 - i) 

        return ans