class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        expectation = 1
        r_sum = 0
        patches = 0
        j = 0
        while expectation < n + 1:

            while j < len(nums) and nums[j] <= expectation:
                r_sum += nums[j]
                j += 1

            if r_sum < expectation:
                patches += 1
                r_sum += expectation
            
            expectation = r_sum + 1

        return patches
               