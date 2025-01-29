# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        its, rem = divmod(target, sum(nums))
        if rem == 0:
            return its * len(nums)
        
        dct = {0: -1}
        res = float('inf')
        r_sum = 0
        nums += nums
        for i in range(len(nums)):
            r_sum += nums[i]
            dct[r_sum] = i
            comp = r_sum - rem
            if comp in dct:
                res = min(res, i-dct[comp])

        return (its * len(nums) // 2) + res if res < float('inf') else -1
