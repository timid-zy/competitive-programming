class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:    
        newArr = [0] * len(nums)
        mid = len(nums) // 2
        pos = 0
        neg = 0
        for i in range(0, len(nums), 2):
            while pos < len(nums) and nums[pos] < 0:
                pos += 1
            while neg < len(nums) and nums[neg] > 0:
                neg += 1
            newArr[i + 1] = nums[neg]
            newArr[i] = nums[pos]
            pos += 1
            neg += 1

        return newArr