# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort(arr):
            for i in range(len(arr)):
                for j in range(len(arr) - i - 1):
                    if int(nums[j] + nums[j+1]) > int(nums[j+1] + nums[j]):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        
        nums = list(map(str, nums))
        sort(nums)
        return str(int("".join(nums[::-1])))
