class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_order(arr):
            for i in range(len(nums)):
                for j in range(len(nums) - i - 1):
                    if int(nums[j] + nums[j+1]) > int(nums[j+1] + nums[j]):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        
        nums = list(map(str, nums))
        custom_order(nums)
        final_num = ""
        for i in range(len(nums)-1, -1, -1):
            final_num += nums[i]
        return str(int(final_num))