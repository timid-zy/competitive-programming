# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        p = res = bc = 0
        for i in range(max(nums) + 1):
            res += bc
            bc -= 1
            while p < len(nums) and nums[p] == i:
                p += 1; bc += 1
            else:
                bc = max(0, bc)
        
        return res + bc*(bc+1) // 2
            