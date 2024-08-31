class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        good_position = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= good_position:
                good_position = i
        
        return True if good_position == 0 else False