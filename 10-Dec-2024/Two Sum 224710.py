# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in rs:
                return [rs[t], i]
            
            rs[n] = i