class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict1 = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict1:
                dict1[sorted_nums[i]] = i
            
        for i in range(len(nums)):
            nums[i] = dict1[nums[i]]
        return nums