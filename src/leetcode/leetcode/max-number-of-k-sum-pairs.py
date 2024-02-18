class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        start = 0
        end = len(nums) - 1
        operations = 0

        while start < end:
            curr_sum = nums[start] + nums[end]
            if curr_sum == k:
                operations += 1
                start += 1
                end -= 1
            elif curr_sum > k:
                end -= 1
            else:
                start += 1
        
        return operations