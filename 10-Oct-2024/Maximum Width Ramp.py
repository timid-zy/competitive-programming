class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        I = {}
        for i, n in enumerate(nums):
            if len(stk) == 0 or stk[-1] > n:
                stk.append(n)
                I[n] = i
        
        res = 0
        stk = stk[::-1]
        for i in range(1, len(nums)):
            j = bisect_right(stk, nums[i]) - 1
            if j == -1:
                continue
            
            res = max(res, i - I[stk[j]])
        
        return res