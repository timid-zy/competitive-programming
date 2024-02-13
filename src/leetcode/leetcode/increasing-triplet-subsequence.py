class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        min_1 = nums[0]
        min_2 = nums[1]
        min_target = min_2 + 1

        if min_2 <= min_1:
            min_1 = nums[1]
            min_2 = float('inf')
            min_target = float('inf')        

        for i in range(2, len(nums)):
            if nums[i] >= min_target:
                return True
            elif nums[i] < min_1:
                min_1 = nums[i]
                min_2 = float('inf')
            elif nums[i] < min_2 and nums[i] > min_1:
                min_2 = nums[i]
                min_target = min(min_target, min_2 + 1)
        
        return False