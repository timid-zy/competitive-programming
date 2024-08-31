class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return nums
        zeroPos = nums.index(0)
        i = zeroPos + 1
        while i < len(nums) and zeroPos < len(nums):
            if nums[i] != 0:
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos += 1
                i = zeroPos + 1
            else:
                i += 1
        