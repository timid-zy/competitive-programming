class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        total_pairs = 0
        i = 0
        j = 1
        while i < len(nums):
            if j < len(nums) and sorted_nums[i] + sorted_nums[j] < target:
                total_pairs += 1
                j += 1
            else:
                i += 1
                j = i + 1
        return total_pairs