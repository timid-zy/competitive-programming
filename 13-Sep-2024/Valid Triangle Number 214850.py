# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            l, r = 0, i-1
            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    res += r - l
                    r -= 1
                else:
                    l += 1

        return res
    