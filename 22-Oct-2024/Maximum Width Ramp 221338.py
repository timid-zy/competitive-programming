# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        idx = []
        for i in range(len(nums)):
            if not stk or stk[-1] > nums[i]:
                stk.append(nums[i])
                idx.append(i)
        
        stk = stk[::-1]
        idx = idx[::-1]
        res = float('-inf')
        for i in range(1, len(nums)):
            li = bisect.bisect_right(stk, nums[i])
            res = max(res, i - idx[li-1])
        
        return res