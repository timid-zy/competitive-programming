# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {nums[i]: i for i in range(len(nums))}
        for x, y in operations:
            mp[y] = mp[x]
            del mp[x]

        res = [None] * len(nums)
        for k, v in mp.items():
            res[v] = k

        return res 