class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1 = set()
        for i in range(len(nums)):
            pre_len = len(set1)
            set1.add(nums[i])
            if len(set1) == pre_len:
                return nums[i]