class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        operations = 0
        i = 0
        multiplier = 0
        count = 1
        smallest = sorted_nums[0]
        while i < len(nums):
            if sorted_nums[i] == smallest:
                i += 1
                continue
            elif sorted_nums[i] != sorted_nums[i-1]:
                operations += count * multiplier
                multiplier += 1
                count = 1
            else:
                count += 1
            i += 1
        return operations + count*multiplier 