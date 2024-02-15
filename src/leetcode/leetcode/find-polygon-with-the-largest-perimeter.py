class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        max_perimeter = -1
        r_sum = 0
        for i in range(len(nums)):
            if r_sum > nums[i]:
                max_perimeter = max(max_perimeter, r_sum + nums[i])
            r_sum += nums[i]

        return max_perimeter