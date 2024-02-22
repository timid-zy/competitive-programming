import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        min_val = nums[-1]
        count = 0
        for i in range(len(nums) -2, -1, -1):
            if min_val >= nums[i]:
                min_val = nums[i]
                continue
            
            spaces = math.ceil(nums[i] / min_val)
            min_val = nums[i] // spaces
            count += spaces - 1

        return count
        # min_val = nums[-1]
        # count = 0
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] <= min_val:
        #         min_val = nums[i]
        #         continue

        #     div = (nums[i] // min_val)

        #     if div == 1:
        #         count += 1
        #         min_val = nums[i] // 2
            
        #     elif div > 1:
        #         count += div - 1
        #         div = (nums[i] % min_val) + min_val
        #         if div == min_val:
        #             continue
        #         count += 1
        #         min_val = div // 2

        # return count