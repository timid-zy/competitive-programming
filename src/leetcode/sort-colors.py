class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict1 = {
            0: 0,
            1: 0,
            2: 0
        }

        for i in range(len(nums)):
            dict1[nums[i]] += 1
        
        pos = 0
        for key in dict1:
            for i in range(dict1[key]):
                nums[pos] = key
                pos += 1