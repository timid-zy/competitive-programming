class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        reverseSum = [0] * len(nums)
        reverseSum[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i])
            reverseSum[len(nums) - 1 - i] = reverseSum[len(nums) - i] + nums[len(nums) - 1 - i]

        for i in range(len(prefixSum)):
            if prefixSum[i] == reverseSum[i]:
                return i
        return -1