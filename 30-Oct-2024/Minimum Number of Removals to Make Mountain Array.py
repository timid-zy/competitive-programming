class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis(nums):
            lis = [1] * len(nums)
            stk = []
            for i, n in enumerate(nums):
                if stk and stk[-1] >= n:
                    idx = bisect.bisect_left(stk, n)
                    stk[idx] = n
                    lis[i] = idx + 1
                else:
                    lis[i] = len(stk) + 1
                    stk.append(n)

            return lis
        
        dpf, dpr = lis(nums), lis(nums[::-1])[::-1]
        res = len(nums)
        for i in range(len(nums)):
            if dpf[i] > 1 and dpr[i] > 1:
                res = min(res, len(nums) - dpf[i] - dpr[i] + 1)

        return res