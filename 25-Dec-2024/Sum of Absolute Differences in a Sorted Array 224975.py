# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        r = 0
        results = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            s -= nums[i]
            results[i] = r - s + nums[i] * (2*i - len(nums) + 1) 
            r += nums[i]
        
        return results