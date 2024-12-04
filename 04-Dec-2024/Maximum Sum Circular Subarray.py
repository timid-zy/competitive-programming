class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        rmn = rmx = 0
        mx = mn = nums[0]
        for n in nums:
            if rmn > 0: rmn = 0
            if rmx < 0: rmx = 0
            rmx += n
            rmn += n
            mn = min(rmn, mn)
            mx = max(rmx, mx)
        
        total = sum(nums) - mn
        if total == 0:
            return mx

        return max(mx, total)