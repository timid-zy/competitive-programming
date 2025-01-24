# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        t = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                t += 1
                if t > 1: return False
                
                if i == len(nums)-2 or nums[i+2] >= nums[i]:
                    nums[i+1] = nums[i]
                elif i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    return False

        return True